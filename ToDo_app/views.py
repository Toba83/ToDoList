from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from ToDo_app.models import Task


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Task_list(request):
    tasks = Task.objects.all()
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

def Task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'task/task_detail.html', context)