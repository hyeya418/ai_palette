from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/summary/', views.summary_view, name='perfect-summary'),
    path('services/ppt-draft/', views.ppt_draft_view, name='ppt-draft'),
    path('services/presentation-script/', views.presentation_script_view, name='presentation-script'),
    path('services/interview-prep/', views.interview_prep_view, name='interview-prep'),
    path('services/pdf-chatbot/', views.pdf_chatbot_view, name='pdf-chatbot'),
    
    path('upload-files/', views.upload_files, name='upload_files'),
    path('vectorize/', views.initiate_vectorization, name='initiate_vectorization'),


]