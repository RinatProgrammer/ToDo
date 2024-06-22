# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.create_todo_item, name='create_todo_item'),
    path('update/<pk>/', views.update_todo_item, name='update_todo_item'),
    path('delete/<pk>/', views.delete_todo_item, name='delete_todo_item'),
]