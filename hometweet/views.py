from multiprocessing import context
from urllib.request import Request
from django.dispatch import receiver
from django.shortcuts import render
from .models import Tweet
from .forms import make_tweet_form
from django.contrib.auth.models import User

# Create your views here.
def home_view(request, id):
    tweets = Tweet.objects.get(id=id)
    context = {"tweets": tweets}
    return render(request, "hometweet/displaytweets.html", context)


def make_tweet_view(request):
    form = make_tweet_form(request.POST or None)
    if form.is_valid():
        form.save()
    form = make_tweet_form()
    context= {'forms': form}
    return render(request, "hometweet/home.html", context)


# def profile_view(request, id):
#     profile = Profile.objects.get(id=id)
#     relationship = Relationship.objects.filter(status = "send", receiver= id)
#     print(relationship)
#     user = request.user
#     for prof in profile.friends.all():
#         if user not in prof: 
        

#     context = {"profile": profile}
#     return render(request, "hometweet/profile.html", context)

'''test view'''
# def home_view(request):
#     # tweets = Tweets.objects.all()
#     # context = {"tweets": tweets}
#     return render(request, "hometweet/displaytweets.html", {})