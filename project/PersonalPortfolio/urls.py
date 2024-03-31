from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    path('project/', TemplateView.as_view(template_name='project.html'), name='project'),
]
