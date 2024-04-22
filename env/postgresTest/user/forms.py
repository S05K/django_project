from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from user.models import CustomUser

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "username", "email","password", "image" ]

    def clean(self):
        super(UserForm, self).clean()

        password = self.cleaned_data.get('password')
        user_email = self.cleaned_data.get('email')

        if(len(password)<6):
            self._errors['password'] = self.error_class(['Password length should not be less than 6 characters'])
            return self.cleaned_data
        
        if CustomUser.objects.filter(email=user_email).exists():
            self._errors['email'] = self.error_class(['Email has already taken'])
            return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    