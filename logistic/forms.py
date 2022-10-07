from dataclasses import field
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'tg_username', 'password1', 'password2']

