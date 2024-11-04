from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Hlavní stránka
    path('add_horse/', views.add_horse, name='add_horse'),
    path('add_care/', views.add_care, name='add_care'),
    path('add_training/', views.add_training, name='add_training'),
    path('horses/', views.horse_list, name='horse_list'),  # Seznam koní
    path('horses/<int:horse_id>/', views.horse_detail, name='horse_detail'),  # Detail koně
]
