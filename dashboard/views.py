from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction

from .models import UploadedFile, VectorFile
from .services import (
    process_uploaded_file, 
    save_faiss_index, 
    load_faiss_index
    )


def home_view(request):
    return render(request, 'dashboard/home.html')

def summary_view(request):
    return render(request, 'dashboard/summary.html')

def ppt_draft_view(request):
    return render(request, 'dashboard/ppt_draft.html')

def presentation_script_view(request):
    return render(request, 'dashboard/presentation_script.html')

def interview_prep_view(request):
    return render(request, 'dashboard/interview_prep.html')

def pdf_chatbot_view(request):
    return render(request, 'dashboard/pdf_chatbot.html')

def upload_files(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('file')
        doc_no = request.POST.get('doc_no')  # 보고서 번호 받아오기

        for uploaded_file in uploaded_files:
            # 새 UploadedFile 객체를 생성하고, 추가 필드가 자동으로 채워지도록 저장합니다
            uploaded_file_obj = UploadedFile(
                file=uploaded_file,
                doc_no=doc_no
            )
            uploaded_file_obj.save()  # 커스텀 save() 메서드를 호출하여 추가 필드를 자동으로 채움

        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'No files uploaded.'})


def initiate_vectorization(request):
    if request.method == 'POST':
        doc_no = request.POST.get('doc_no') 
        result = vectorize_and_save_faiss(doc_no)

        if result['success']:
            return JsonResponse({'success': True, 'vector_file_path': result['vector_file_path']})
        else:
            return JsonResponse({'success': False, 'error': result['error']})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def vectorize_and_save_faiss(doc_no):
    """
    주어진 문서 번호 (doc_no)에 해당하는 모든 업로드 파일을 벡터화하고 FAISS 인덱스에 저장하는 함수.
    벡터 파일 경로는 VectorFile 모델에 저장.
    """
    # doc_no에 해당하는 모든 파일을 조회
    file_instances = UploadedFile.objects.filter(doc_no=doc_no)

    if not file_instances.exists():
        return {'success': False, 'error': 'No files found for the given doc_no'}

    all_documents = []

    # 업로드된 파일들을 벡터화
    for file_instance in file_instances:
        documents = process_uploaded_file(file_instance.file.path)
        all_documents.extend(documents)

    # 벡터화된 문서들을 FAISS 인덱스에 저장
    index_file_path = save_faiss_index(all_documents, doc_no)

    # 트랜잭션 사용하여 삽입 또는 업데이트
    with transaction.atomic():
        vector_file, created = VectorFile.objects.update_or_create(
            doc_no=doc_no,
            defaults={'vector_file_path': index_file_path}
        )

    return {'success': True, 'vector_file_path': index_file_path}
