from django.shortcuts import render
from .models import AIService

def dashboard_view(request):
    # 데이터베이스에서 모든 AI 서비스를 가져옵니다.
    services = AIService.objects.all()
    return render(request, 'dashboard/dashboard.html', {'services': services})

def dashboard_view(request):
    menu_items = [
        {"id": "home", "name": "홈"},
        {"id": "reports", "name": "레포트"},
        {"id": "character-chat", "name": "캐릭터 챗"},
        {"id": "ppt-draft", "name": "PPT 초안"},
        {"id": "summary", "name": "완벽 요약"},
    ]
    return render(request, 'dashboard/dashboard.html', {'menu_items': menu_items})
