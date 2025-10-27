from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'L', 'Low'
        MEDIUM = 'M', 'Medium'
        HIGH = 'H', 'High'

    title = models.CharField(max_length= 250)
    description = models.TextField()
    slug = models.SlugField(max_length= 250, unique= True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)

    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10,
                                choices=Priority.choices,
                                default=Priority.MEDIUM
                                )

    task_user = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='tasks'
                                  )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = f'{self.task_user.username}-{slugify(self.title)}'
            slug = base_slug.lower()
            counter = 1

            while Task.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = slug
        super(Task, self).save(*args, **kwargs)

    def complete_status(self):
        return 'completed' if self.completed else 'not completed'

    def get_absolute_url(self):
        return reverse('todo_app:task_detail', args= [self.pk])

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields= ['-created_at']),
        ]

    def __str__(self):
        return self.title
