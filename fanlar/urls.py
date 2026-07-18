from django.urls import path
from . import views

app_name = "fanlar"

urlpatterns = [
    path('', views.fanlar_list, name='fanlar_list'),
    path('create/', views.fanlar_create, name='fanlar_create'),
    path('update/<int:id>/', views.fanlar_update, name='fanlar_update'),
    path('delete/<int:id>/', views.fanlar_delete, name='fanlar_delete'),
    path('sotib-olish/<int:id>/', views.fan_sotib_olish, name='fan_sotib_olish'),
    path('darsliklar/<int:id>/', views.darsliklar_kirish, name='darsliklar_kirish')
]