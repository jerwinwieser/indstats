from django.urls import path
from core import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('create/', views.application_create, name='application_create'),
    path('statistics/', views.statistics, name='statistics'),
]