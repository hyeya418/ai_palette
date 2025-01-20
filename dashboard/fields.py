from django.db import models

# 삭제 여부 필드
class DelYnFieldMixin(models.Model):
    YES_NO_CHOICES = [
        ('y', 'Yes'),
        ('n', 'No'),
    ]
    del_yn = models.CharField(
        max_length=1,
        choices=YES_NO_CHOICES,
        default='n',
        verbose_name="삭제 여부"
    )

    class Meta:
        abstract = True  # 데이터베이스 테이블 생성 안 함


# 노출 순서 필드
class DisplayOrderFieldMixin(models.Model):
    display_order = models.IntegerField(
        default=0,
        verbose_name="노출 순서"
    )

    class Meta:
        abstract = True


# 수정 일시 필드
class UpdatedAtFieldMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="수정 일시"
    )

    class Meta:
        abstract = True


# 생성 일시 필드
class CreatedAtFieldMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성 일시"
    )

    class Meta:
        abstract = True
