from unittest.util import _MAX_LENGTH
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


