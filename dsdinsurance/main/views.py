from django.shortcuts import render
from .models import Customers

# Create your views here.
from django.http import HttpResponse


def index(request):
    customers = Customers.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'customers': customers})


def about(request):
    return render(request, "main/about.html")


def calculator(request):
    return render(request, "main/calculator.html")


def benefits(request):
    return render(request, "main/benefits.html")


def partners(request):
    return render(request, "main/partners.html")


def feedback(request):
    return render(request, "main/feedback.html")


def contact(request):
    return render(request, "main/contact.html")

