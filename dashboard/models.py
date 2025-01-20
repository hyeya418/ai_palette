import os
from django.db import models
from .fields import (
    CreatedAtFieldMixin,
)


class AIService(models.Model):
    tagid = models.CharField(max_length=50, unique=True)  # HTML 태그 id로 사용될 값
    name = models.CharField(max_length=100)  # 서비스 이름
    description = models.TextField(blank=True)  # 서비스 설명
    path = models.CharField(max_length=100, unique=True)  # 경로 필드
    icon = models.ImageField(upload_to='icons/', blank=True)  # 아이콘
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜

    def __str__(self):
        return self.name
    
# UploadedFile 모델
class UploadedFile(CreatedAtFieldMixin):
    uploaded_file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='uploads/', verbose_name="파일")
    origin_filename = models.CharField(max_length=255, verbose_name="원본 파일명")
    attach_filename = models.CharField(max_length=255, verbose_name="첨부 파일명")
    file_path = models.CharField(max_length=255, verbose_name="파일 경로")
    attach_ext = models.CharField(max_length=10, verbose_name="파일 확장자")
    file_size = models.BigIntegerField(verbose_name="파일 크기")
    doc_no = models.BigIntegerField(verbose_name="문서 번호")

    class Meta:
        db_table = 'tb_uploaded_file'
        verbose_name = '업로드된 파일'
        verbose_name_plural = '업로드된 파일들'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.origin_filename = os.path.basename(self.file.name)
        self.file_path = self.file.url
        self.attach_ext = os.path.splitext(self.file.name)[1]
        self.file_size = self.file.size
        self.attach_filename = self.file.name
        super().save(*args, **kwargs)

# VectorFile 모델
class VectorFile(models.Model):
    vector_file_id = models.AutoField(primary_key=True)
    doc_no = models.BigIntegerField(verbose_name="문서 번호")
    vector_file_path = models.CharField(max_length=255, verbose_name="벡터 파일 경로")

    class Meta:
        db_table = 'tb_vector_file'
        verbose_name = '벡터 파일'
        verbose_name_plural = '벡터 파일들'
