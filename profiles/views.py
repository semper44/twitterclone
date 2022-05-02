from multiprocessing import context
import profile
import re
from django.dispatch import receiver
from django.shortcuts import redirect, render

from .models import Profile, Relationship
from . forms import register_form
from django.contrib.auth import authenticate, login,logout
from hometweet.models import Tweet
from django.contrib.auth.models import User


# Create your views here.
def register_view(request):
    form = register_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    form = register_form()
    context = {"form": form}
    return render(request, "profiles/register.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
    return render(request, "profiles/login.html", {})

'''view friends tweet view'''
def profile_view(request):
    idd = request.user.id
    print(idd)
    profiles = Profile.objects.get(id=idd)
    friend = profiles.friends.all()
    posts = []
    for f in friend:
        tweet = Tweet.objects.filter(id= f.id)
        for i in tweet:
            posts.append(i)
    context = {"posts":posts}
    
    return render(request, "profiles/profile.html", context)

'''my friends list''' 
pals = []
def view_friends(request):
    idd = request.user.id
    profile= Profile.objects.get(id = idd)
    print(profile)
    friend =  profile.friends.all()
    print(friend)
    context = {"friend": friend}
    return render(request, "profiles/friends.html", context)

'''find friends list'''
def find_friends(request):
    id = request.user.id
    all_profiles = Profile.objects.exclude(id = id)
    user = Profile.objects.get(id = id)
    friends = user.friends.exclude(id = id)
    profile_list = []
    friends_list = []

    for f in friends:
        friends_list.append(f.id)
    
    
    for p in all_profiles:
        profile_list.append(p.id)               
    
    print(profile_list)

    for i in profile_list:
        if i not in friends_list:
            print(i) 

    context = {
        "friends_list": friends_list,
        "profile_list": "profile_list"
    }
    return render(request, "profiles/find_friends.html", context)

def remove_friend_view(request):
    idd = request.user.id
    prof=Profile.objects.get(id = 4)
    # rel = prof.relationship_set.
    profiles = Relationship.objects.get(id= 3)
    # rel = profiles.receiver_id.all()
    # rel = profiles.filter
    print(profiles.receiver_id)
    # rel= profiles.status.all()
    print(idd)
    # rel = profiles.status.filter(id = id, status = "accept")
    # print(rel)
    context = {"delete": "delete" }
    return render(request, "profiles/removefriends.html", context)



def add_friend_view(request, id):
    if "add" in request.POST:
        user = request.user
        friend = Profile.objects.get(user= user)
        profiles = Profile.objects.get(id=5)
        # profiles = friend.friends.get(id=id)
        print(profiles)
        print(friend)
        Rel= Relationship.objects.create(sender = friend, receiver = profiles, status = "send")
    context = {"delete": "delete" }
    return render(request, "profiles/addfriends.html", context)
