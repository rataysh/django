from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):  # HttpRequest
    return HttpResponse("Page women app")


def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>list categories</h1><p>{catid}")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по городам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена, не растраивайтесь)</h1>')