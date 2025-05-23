from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
    