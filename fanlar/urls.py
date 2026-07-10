from django.urls import path
from . import views

urlpatterns = [
    path('', views.fanlar_list, name='fanlar_list'),
    path('create/', views.fanlar_create, name='fanlar_create'),
    path('update/<int:id>/', views.fanlar_update, name='fanlar_update'),
    path('delete/<int:id>/', views.fanlar_delete, name='fanlar_delete'),
    path('darslik_list/<int:id>/', views.darslik_kirish, name='darslik_list')
]