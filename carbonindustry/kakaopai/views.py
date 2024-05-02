from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "kakaopai/map.html")
    # return HttpResponse("하이~")
