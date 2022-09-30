from os import access
from django.shortcuts import render
from django.http import HttpResponse
from .models import Accounts


def index(request):
    # print("=------>",.objects.all())
    return HttpResponse("Hello, world. You're at the polls index.")