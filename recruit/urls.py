from django.urls import path

from . import views

# URL namespace지정
app_name = "recruit"

urlpatterns = [
    path("/recruit_list", views.recruit_list, name="list"),
    path("/recruit/<int:pk>/", views.recruit_detail, name="detail"),
    path("/recruit/create/", views.recruit_create, name="create"),
    path("/recruit/<int:pk>/update/", views.recruit_update, name="update"),
    path("/recruit/<int:pk>/delete/", views.recruit_delete, name="delete"),
]
