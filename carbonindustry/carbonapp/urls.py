from django.urls import path
from . import views

app_name = 'carbonfarm'

urlpatterns = [
    path('', views.BoardList.as_view(), name='list'),
    path('create/', views.BoardCreate.as_view(), name='create'),

]
