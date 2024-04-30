from django import forms
from .models import Board


class BoardForm(forms.ModelForm):  # 유효성 검증은 아직 안한 상태
    class Meta:
        model = Board  # 데이터는 보드를 쓰겠다
        fields = ["title", "writer", "content"]  # 필드는 이거 3개의 형태를 받겠다.
