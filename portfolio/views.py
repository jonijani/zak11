from django.shortcuts import render
from .models import Project

def home(request):
    hello = Project.objects.all()
    return render(request,'portfolio/home.html',{'hi':hello})

# Create your views here.
