from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks, name='tasks'),
    path('contact/', views.contact, name='contact'),

    path('tasks/count/', views.task_count, name='task_count'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),

    path('hello/<str:name>/', views.hello, name='hello'),
]