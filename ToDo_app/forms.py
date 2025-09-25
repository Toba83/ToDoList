from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title','description','priority']

class TaskEditForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title','description','priority','completed']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, required=True)
    password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)