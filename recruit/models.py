from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Recruit(models.Model):
    company_name = models.CharField(max_length=50, help_text="채용 회사명")
    title = models.CharField(max_length=50, help_text="채용 공고 제목")
    description = models.CharField(max_length=255, help_text="채용 공고 상세 설명")
    post_at = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField()

    class Meta:
        ordering = ["-post_at"]
        verbose_name = "채용 공고"
        verbose_name_plural = "채용 공고들"

    def __str__(self):
        return f"{self.company_name} - {self.title}"

    def clean(self):
        if self.closing_date <= timezone.now():
            raise ValidationError("마감일은 현재 시간보다 미래여야 합니다.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
