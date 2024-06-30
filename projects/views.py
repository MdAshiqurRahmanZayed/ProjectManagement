from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, TaskForm,TaskUpdateForm
from .models import Project, Task



@login_required
def home(request):
     projects = Project.objects.filter(members=request.user)
     return render(request, 'projects/home.html', {'projects': projects})


@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.user not in project.members.all():
        return redirect('projects:home')
    tasks = project.tasks_project.all()
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            form.save_m2m()
            return redirect('projects:home')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:home')  
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'project': project})


@login_required
def task_create(request, pk):
    
    
    project = get_object_or_404(Project, pk=pk)
    
    if request.user not in project.members.all():
        
        return redirect('project_list')
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('projects:project_detail', id=project.pk)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form,'project':project})

@login_required
def update_task(request, p_pk,t_pk):
    task = get_object_or_404(Task, pk=t_pk)    
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('projects:project_detail', id=p_pk) 
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'task': task})
