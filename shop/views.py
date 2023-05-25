from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Category, Product

def about_shop(request):
    return HttpResponse("Page about ComputerShop")

def contacts(request):
    return HttpResponse("Contacts ComputerShop")