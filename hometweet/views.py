from django.shortcuts import render
from .models import Post, Coment, Reaction, Reply
from .forms import make_tweet_form, Reply_form, comment_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from profiles.models import Profile

# Create your views here.
def home_view(request):
    user = request.user
    profiles = Profile.objects.get(user = user)
    friend = profiles.friends.all()
    tweets =  Post.objects.all()
    friends_id = []

    for i in friend:
        friends_id.append(i.id)
    context = {"friend_id": friends_id, "tweets":tweets}
    return render(request, "hometweet/home.html", context)

@login_required(login_url="login")
def make_tweet_view(request):
    author = request.user
    form = make_tweet_form(initial={"author": author})
    if request.method == "POST":
        form = make_tweet_form(request.POST or None)
        if form.is_valid():
            form.save()
    context= {'forms': form}
    return render(request, "hometweet/make-tweet.html", context)

# def home_view(request):
#     author = request.user
#     form = make_tweet_form()
#     # context = {"tweets": tweets}
#     return render(request, "hometweet/home.html", {})

def post_list_view(request, id):
    posts = Post.objects.get(id = id)
    user = request.user
    forms= comment_form(initial={"comment_author": user, "comment_post":posts})
    if request.method == "POST":
        forms= comment_form(request.POST or None)
        if forms.is_valid():
            forms.save()
    context = {"forms": forms, "post": posts}
    return render(request, "hometweet/comment.html", context)

def reply_view(request):
    comment = Coment.objects.all()
    user = request.user
    form = Reply_form(request.POST or None, instance = user)
    if form.is_valid():
        form.save()
    context = {"comment_author": comment, "form": form }
    return render(request, "hometweet/home.html", {})