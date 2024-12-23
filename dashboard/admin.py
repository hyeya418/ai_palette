from django.contrib import admin
from .models import AIService

@admin.register(AIService)
class AIServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon', 'url', 'created_at')