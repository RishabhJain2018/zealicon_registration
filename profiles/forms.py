from django import forms
from .models import UserDetail
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        exclude = ['username']


class UserDetailForm(forms.ModelForm):

    class Meta:
        model = UserDetail
        exclude = ['user']
