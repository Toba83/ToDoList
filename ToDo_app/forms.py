from django import forms
from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        labels = {
            'title': 'عنوان تسک',
            'description': 'توضیحات',
            'due_date': 'فرصت',
            'priority': 'اولویت',
        }
        help_texts = {
            'priority': 'اولویت را از کم تا زیاد مشخص کنید',
        }


class TaskEditForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'completed', 'due_date']


class LoginForm(forms.Form):
    username = forms.CharField(max_length= 250, required= True)
    password = forms.CharField(max_length= 250, required= True, widget= forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length= 250, required= True, widget= forms.PasswordInput)
    password_repeat = forms.CharField(max_length= 250, required= True, widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password1(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise forms.ValidationError('password and password_repeat dont match')
