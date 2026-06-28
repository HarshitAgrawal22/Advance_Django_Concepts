from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

from . import views

urlpatterns = [
    path("", lambda x: JsonResponse({"rabdi": f"{x}"})),
    path("bad_response/", views.bad_response),
    path("test_page/", views.test_page),
    path("home_page/", views.home_page),
]
