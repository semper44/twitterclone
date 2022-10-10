# from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Coment, Post, Reply


class make_tweet_form(ModelForm):
    class Meta:
        model = Post
        fields = ["author", "content", "pics"]

class comment_form(ModelForm):
    class Meta:
        model = Coment
        fields = "__all__"

class Reply_form(ModelForm):
    class Meta:
        models =  Reply
        fields = ["reply_comments","reply_author","reply","reply_pics","date_created"]