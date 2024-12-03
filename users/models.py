from django.db import models
from django.db.models import UniqueConstraint


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    phone_number = models.CharField(max_length=50)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    self_introduced = models.TextField(blank=True, null=True)
    portfolio = models.BinaryField(null=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.user_name
