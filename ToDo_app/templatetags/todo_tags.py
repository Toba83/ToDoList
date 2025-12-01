from datetime import timedelta

from django import template
from django.utils import timezone

from ..models import *

register = template.Library()

@register.simple_tag()
def total_tasks(user):
    return Task.objects.filter(task_user= user).count()

@register.simple_tag()
def total_completed_tasks(user):
    return Task.objects.filter(completed= True, task_user= user).count()

@register.simple_tag()
def total_uncompleted_tasks(user):
    return Task.objects.filter(completed= False, task_user= user).count()

@register.inclusion_tag('partial/today_tasks.html')
def today_tasks(user):
    today_task = Task.objects.filter(due_date= timezone.now(), task_user= user)
    context = {
        'today_task': today_task
        }
    return context

@register.simple_tag()
def expired_tasks(user):
    return Task.objects.filter(due_date__lt= timezone.now(), task_user= user).count()

@register.inclusion_tag('partial/last_week.html')
def last_week(user):
    now = timezone.now()
    lw = now + timedelta(days=7)

    last_week_tasks = Task.objects.filter(due_date= now, due_date__lte= lw, task_user= user)
    context = {
        'last_week_tasks': last_week_tasks
    }
    return context