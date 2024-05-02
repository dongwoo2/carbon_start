from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Board
from .forms import BoardUpdateForm
from .forms import BoardSearchForm
from .forms import BoardForm
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django.db.models import Q  # or 연산을 위해 import

# Create your views here.


class BoardList(generic.ListView):  # 리스트
    model = Board
    ordering = ["-pk"]

    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = BoardSearchForm()  # 파라미터 추가
        return context


class BoardCreate(generic.CreateView):
    model = Board  # 보드 모델을 쓰겠다
    form_class = BoardForm  # 폼은 이거 쓰겠다.
    success_url = reverse_lazy("carbonfarm:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # 부모가 가지고 있는 기존 컨텍스트 정보
        context["button_label"] = "등록"  # 새로운 값 추가
        return context


class BoardDetail(generic.DetailView):
    model = Board  # 모델은 보드로 쓰겠다

    def get_object(self):  # 재정의
        item = super().get_object()
        item.increment_read_count()
        return item


class BoardUpdate(generic.UpdateView):
    model = Board
    form_class = BoardUpdateForm

    def get_success_url(self):
        return reverse("carbonfarm:detail", args=(self.object.id,))

    def get_context_data(
        self, **kwargs: any
    ) -> dict[str, any]:  # > dict[str, any] 는 반환자료형이 무엇인지 명시해주는 것 글등록에 있는 함수처럼 없어도 무관함
        context = super().get_context_data(**kwargs)
        context["button_label"] = "수정"  # 파라미터를 추가해주는 것
        return context


class BoardDelete(generic.DeleteView):
    model = Board
    success_url = reverse_lazy("carbonfarm:list")


class BoardSearch(generic.ListView):
    model = Board
    paginate_by = 3
    # object_list_count = 0 # 검색된 결과 갯수를 나타나기 위해서

    def get_queryset(self):
        keyword = self.request.GET.get(
            "keyword"
        )  # 사용자가 요청하면서 전달한 파라미터 겟 안에서 keyword라는 파라미터를 꺼냄
        if keyword:
            object_list = Board.objects.filter(
                Q(title__icontains=keyword)
                | Q(  # 대소문자 무시 icontains
                    content__icontains=keyword
                )  # title 과 content에 keyword가 들어간다면
            ).order_by("-pk")
            self.object_list_size = object_list.count()
            return object_list  # 이 데이터가 결국 밑에 있는 context_data에 들어감
        else:
            return Board.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = BoardSearchForm()
        context["keyword"] = self.request.GET.get("keyword")
        context["object_list_size"] = self.object_list_size
        return context
