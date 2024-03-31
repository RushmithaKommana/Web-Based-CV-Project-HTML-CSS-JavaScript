from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the home page!</h1>")

def about_view(request):
    return HttpResponse("<h1>This is the about page.</h1>")

def portfolio_view(request):
    return HttpResponse("<h1>This is the portfolio page.</h1>")

def project_view(request):
    return HttpResponse("<h1>This is the project page.</h1>")