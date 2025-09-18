from django.contrib import admin

from ToDo_app.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'task_user', 'completed', 'priority']
    prepopulated_fields = {'slug': ('title',)}