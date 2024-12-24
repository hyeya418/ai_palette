from django.db import models

class AIService(models.Model):
    tagid = models.CharField(max_length=50, unique=True)  # HTML 태그 id로 사용될 값
    name = models.CharField(max_length=100)  # 서비스 이름
    description = models.TextField(blank=True)  # 서비스 설명
    path = models.CharField(max_length=100, unique=True)  # 경로 필드
    icon = models.ImageField(upload_to='icons/', blank=True)  # 아이콘
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜

    def __str__(self):
        return self.name