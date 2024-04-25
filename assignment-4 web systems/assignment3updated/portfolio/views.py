from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def signout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    context = {
        'name': 'Rushmitha',
        'photo_url': 'static/rush_img.jpg',
        'email': 'rk958@njit.edu',
        'github_link': 'https://github.com/your_github_username',
    }
    return render(request, 'home.html', context)


@login_required
def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def addproject(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectForm()

    context = {
        'form': form
    }
    return render(request, 'add_new.html', context)
