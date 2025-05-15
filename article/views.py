from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    users = ["john", "lox", "petya"]
    return render(request, "articles/articles.html", {"users": users})
