from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pg1'),
    path('pg2', views.basket, name='pg2'),
    path('pg3', views.pg3, name='pg3'),
    path('pg4', views.pg4, name='pg4'), 
    path('pg5', views.pg5, name='pg5'),
]