from django.urls import path
from core import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('statistics/', views.statistics, name='statistics'),
]