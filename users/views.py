from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from users.models import User  # User 모델 import


def users_account(request: HttpRequest) -> HttpResponse:
    return render(request, "users_account.html")
from django.shortcuts import render

