from django.contrib import admin

from ToDo_app.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'task_user', 'completed', 'priority']
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ['title']
    list_editable = ['completed', 'priority']
    list_filter = ['completed', 'priority', 'due_date']
    search_fields = ['title', 'description']
    ordering = ('-due_date',)
    date_hierarchy = 'due_date'
