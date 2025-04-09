from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_exercise, name='add_exercise'),
    path('edit_exercise/<int:pk>/', views.edit_exercise, name='edit_exercise'),
    path('delete_exercise/<int:pk>/', views.delete_exercise, name='delete_exercise'),
]