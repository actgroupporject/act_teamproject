from email.policy import default
from unicodedata import category

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Profile, Recruit


# Main Page
def home(request):
    category = Category.objects.all()
    recruit = Recruit.objects.order_by("-post_at")[:5]  # 최근 5개
    profiles = Profile.objects.order_by("-created_at")[:5]  # 최근 5개

    return render(
        request,
        "home.html",
        {"category": category, "recruit": recruit, "profiles": profiles},
    )


def category_list(request):
    category = Category.objects.all()
    return render(request, "category.html", {"category": category})


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    recruits = Recruit.objects.filter(category=category).order_by("-created_at")

    return render(
        request, "category_details.html", {"category": category, "recruits": recruits}
    )


def add_category(request):
    if request.method == "POST":
        pass
    return render(request, "add_category.html")
