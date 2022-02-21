from django.shortcuts import render
from .models import Inventory

# Create your views here.


def home_view(request):
    items = Inventory.objects.all()
    return render(request, 'myapp/index.html', {'items': items})


def detail_view(request):
    return render(request, 'myapp/detail.html')
