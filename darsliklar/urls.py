from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.darslik_create, name='darslik_create'),
    path('update/<int:id>/', views.darslik_update, name='darslik_update'),
    path('delete/<int:id>/', views.darslik_delete, name='darslik_delete')
]