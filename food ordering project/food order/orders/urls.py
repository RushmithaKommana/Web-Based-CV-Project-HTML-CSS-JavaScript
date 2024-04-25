from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('place_order/', views.place_order, name='place_order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('signup/', views.signup, name='signup'),
    path('accounts/logout/', views.logout, name='logout'),
]
