from django.db import models

class AIService(models.Model):
    name = models.CharField(max_length=100)  # 서비스 이름
    description = models.TextField(blank=True)  # 서비스 설명
    icon = models.ImageField(upload_to='icons/')  # 아이콘
    url = models.URLField()  # 서비스 URL
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜