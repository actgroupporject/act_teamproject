from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Main_Page 경로
    path("", views.home, name="home"),
    path("category/<slug:category_slug>/", views.category, name="category"),
    # Category
    path("category/<slug:category_slug>/", views.category_list, name="category_list"),
    path(
        "category/<slug:category_slug>/", views.category_detail, name="category_detail"
    ),
    path("add-category/", views.add_category, name="add_category"),
]
