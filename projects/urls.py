from django.contrib import admin
from django.urls import path,include
from .views import * 

app_name = 'projects'


urlpatterns = [
    path("", home,name='home'),
    path('projects/<int:id>/', project_detail, name='project_detail'),
    path('projects/update/<int:pk>/', project_update, name='project_update'),
    path('projects/new/', project_create, name='project_create'),
    path('projects/<int:pk>/new-task/', task_create, name='task_create'),
    path('project/<int:p_pk>/task/<int:t_pk>/update/', update_task, name='update_task'),
]
