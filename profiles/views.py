from django.shortcuts import redirect, render
from .models import Profile, Relationship
from .forms import register_form
from django.contrib.auth import authenticate, login,logout
from hometweet.models import Post
from django.contrib.auth.models import User, Group
from django.db.models import Q
from itertools import chain
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import assign_perm,get_group_perms


# abigails code
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

def logout_view(request):
    logout(request)
    return redirect("login")

'''view friends tweet view'''
@login_required(login_url="login")
def profile_view(request):
    idd = request.user.id
    print(idd)
    profiles = Profile.objects.get(id=idd)
    friend = profiles.friends.all()
    posts = []
    for f in friend:
        tweet = Post.objects.filter(id= f.id)
        for i in tweet:
            posts.append(i)
    context = {"posts":posts}
    
    return render(request, "profiles/profile.html", context)

'''my friends list''' 
@login_required(login_url="login")
def view_friends(request):
    user = request.user
    # print(idd)
    profile = Profile.objects.get(user = user)
    # print(profile)
    friend = profile.friends.all()
    for i in friend:
        print(i.id)
    context = {"friend": friend}
    return render(request, "profiles/friends.html", context)

'''find friends list'''
@login_required(login_url="login")
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

@login_required(login_url="login")
def remove_friend_view(request, id):
    if request.method == "POST":
        user = request.user
        print(user.id)
        sender=Profile.objects.get(user = user)
        receiver =Profile.objects.get(id = id)
        rel = Relationship.objects.get(Q(sender=receiver, receiver= sender, status="accept") | Q(sender=sender, receiver=receiver, status="accept"))
    
        print(rel)
        rel.delete()
        return redirect("home")
    context = {"delete": "delete" }
    return render(request, "profiles/removefriends.html", context)



@login_required(login_url="login")
def add_friend_view(request, id):
    if "add" in request.POST:
        user = request.user
        friend = Profile.objects.get(user= user)
        profiles = Profile.objects.get(id=id)
        # profiles = friend.friends.get(id=id)
        print(profiles)
        print(friend)
        Rel= Relationship.objects.create(sender = friend, receiver = profiles, status = "send")
    context = {"delete": "delete" }
    return render(request, "profiles/addfriends.html", context)



def view_sent_request(request):
    user = request.user
    prof =  Profile.objects.get(user = user)
    sent_request = Relationship.objects.filter(status ="send", sender= prof)
    print(sent_request)
    context= {"sent_request":sent_request}
    return render(request,"profiles/removefriends.html", context)

def view_received_request(request):
    user = request.user 
    prof =  Profile.objects.get(user = user)
    received_request = Relationship.objects.filter(status ="send", receiver= prof)
    print(received_request)
    context= {"received_request":received_request}
    return render(request,"profiles/received_request.html", context)

def search_view(request):
    if "query" in request.GET:
        queries = request.GET.get("query")
        profile = Profile.objects.filter(user__username__icontains = queries)
        tweets = Post.objects.filter(content__icontains = queries)
        results= chain(profile, tweets)
    else:
        results = Profile.objects.all().none

    context = {"results":results}        
    return render(request,"profiles/search.html", context)

def block_user_view(request, id):
    if request.method == "POST":
       grouped = Group.objects.get(name="blockedusers")
       friend = Profile.objects.get(id = id)
       user = request.user
       blocker = Profile.objects.get(user = user)
       assign_perm("cant_view_profile", grouped, blocker)
       print(friend)
       friend.group.add(grouped)
       friend.has_perm()

    return render(request, "profiles/blockuser.html", {})

