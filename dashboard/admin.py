from django.contrib import admin
from .models import AIService

@admin.register(AIService)
class AIServiceAdmin(admin.ModelAdmin):
    list_display = ('tagid', 'name', 'description', 'path', 'created_at')
    search_fields = ('name', 'description')  # 검색 기능 추가
    list_filter = ('created_at',)  # 필터 추가