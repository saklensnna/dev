
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('list/', views.listEmployee, name='listEmployee'),
    path('add/', views.addEmployee, name='addEmployee'),
    path('<int:id>/', views.addEmployee, name='edit'),
    path('delete/<int:id>/', views.deleteEmployee, name='deleteEmployee'), 
]
