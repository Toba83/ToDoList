from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ToDo_app.forms import *
from ToDo_app.models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def task_list(request):
    user = request.user
    tasks = Task.objects.filter(task_user=user)
    paginator = Paginator(tasks, 3)
    page_number = request.GET.get('page', 1)
    try:
        tasks = paginator.page(page_number)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context = {
        'tasks': tasks
    }
    return render(request, 'task/task_list.html', context)

def task_detail(request, pk):
    user = request.user
    task = get_object_or_404(Task, pk= pk, task_user=user)
    context = {
        'task': task,
    }
    return render(request, 'task/task_detail.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task_obj = Task.objects.create(title= cd['title'],
                                           description= cd['description'],
                                           priority= cd['priority'],
                                           task_user= request.user,
                                           )
            task_obj.save()
            return redirect('todo_app:task_detail', pk= task_obj.pk)
    else:
        form = TaskForm()
    return render(request, 'forms/task_create.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk= task_id)
    if task.task_user == request.user:
        if request.method == "POST":
            form = TaskEditForm(request.POST, instance= task)
            if form.is_valid():
                task = form.save()
                priority = form.cleaned_data.get('priority')
                if priority:
                    task.priority = priority
                    task.save()
                return redirect('todo_app:profile')
        else:
            form = TaskEditForm(instance= task)
    else:
        return HttpResponse("You are not the owner of this task.")

    return render(request, 'forms/task_edit.html', {'form': form, 'task': task})
def profile(request):
    user = request.user
    tasks = Task.objects.filter(task_user= user)
    context = {
        'tasks': tasks
    }
    return render(request, 'task/profile.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id= task_id)
    if task.task_user == request.user:
        if request.method == 'POST':
            task.delete()
            return redirect('todo_app:profile')
    else:
        return HttpResponse("You are not the owner of this task.")
    return render(request, 'forms/task_delete.html', {'task': task})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username= cd['username'], password= cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('todo_app:profile')
                else:
                    return HttpResponse("Your account has been disabled.")
            else:
                return HttpResponse("you are not logged in.")
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/login.html', context)