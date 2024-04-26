from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Board
# Create your views here.


class BoardList(generic.ListView): # 리스트
    model = Board
    ordering = ['-pk']

from .forms import BoardForm
from django.urls import reverse_lazy

class BoardCreate(generic.CreateView):
    model = Board
    form_class = BoardForm
    success_url = reverse_lazy('carbonfarm:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 부모가 가지고 있는 기존 컨텍스트 정보
        context['button_label'] = '등록' # 새로운 값 추가
        return context
