from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Recruit(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    post_at = models.DateTimeField(auto_now_add=True)
    # closing_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    self_introduction = models.CharField(max_length=255)
    portfolio = models.ImageField(upload_to="portfolio", null=True, blank=True)

    def __str__(self):
        return self.user
