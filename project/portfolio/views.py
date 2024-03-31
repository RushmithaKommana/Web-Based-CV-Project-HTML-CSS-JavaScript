from django.shortcuts import render
from .models import Project

def home(request):
    context = {
        'name': 'Rushmitha',
        'photo_url': 'C:\Users\Rushmitha K\OneDrive\Desktop\is601\project\portfolio\static\rush img (1).jpg',""
        'email': 'rk958@njit.edu',
        'github_link': 'https://github.com/your_github_username',
    }
    return render(request, 'home.html', context)

def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)

def about(request):
    return render(request, 'about.html')
