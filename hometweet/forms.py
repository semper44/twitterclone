# from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Tweet


class make_tweet_form(ModelForm):
    class Meta:
        model = Tweet
        fields = ["content", "pics"]