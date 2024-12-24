from django.shortcuts import render
from django.urls import reverse
from .models import AIService

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