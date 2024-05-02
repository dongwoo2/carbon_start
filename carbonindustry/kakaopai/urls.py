from django.urls import path
from . import views

app_name = "kakaomap"

urlpatterns = [
    path("", views.index),
]
