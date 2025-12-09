from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('join/', views.join_crew, name='join_crew'),
    path('crew/', views.crew_list, name='crew_list'),
]
