from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('add/', views.addproject, name='add'),
    path('accounts/login/', views.signin_view, name='login'),
    path('signout/', views.signout_view, name='signout'),
]
