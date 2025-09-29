from datetime import timedelta

from django import template
from django.utils import timezone

from ..models import *

register = template.Library()

@register.simple_tag()
def total_tasks():
    return Task.objects.count()

@register.simple_tag()
def total_completed_tasks():
    return Task.objects.filter(completed=True).count()

@register.simple_tag()
def total_uncompleted_tasks():
    return Task.objects.filter(completed=False).count()

@register.inclusion_tag('partial/today_tasks.html')
def today_tasks():
    today_task = Task.objects.filter(due_date=timezone.now())
    context = {
        'today_task': today_task
        }
    return context

@register.inclusion_tag('partial/last_week.html')
def last_week():
    now = timezone.now()
    lw = now + timedelta(days=7)

    last_week_tasks = Task.objects.filter(due_date=now, due_date__lte=lw)
    context = {
        'last_week_tasks': last_week_tasks
    }
    return context