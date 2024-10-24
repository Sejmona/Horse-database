from django.urls import path
from . import views

urlpatterns = [
    path('add_horse/', views.add_horse, name='add_horse'),
    path('add_care/', views.add_care, name='add_care'),
    path('add_training/', views.add_training, name='add_training'),
]
