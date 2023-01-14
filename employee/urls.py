from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add/', views.addEmployee, name='add'),
    path('add/addResult/', views.addResult, name='addResult'),

    path('delete/<int:id>/', views.deleteEmployee, name='delete'),

    path('update/<int:id>/', views.updateEmployee, name='update'),
    path('update/<int:id>/updateResult/', views.updateResult, name='updateResult'),
]