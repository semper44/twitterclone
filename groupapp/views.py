from django.shortcuts import render, redirect
from .models import Groupapp
from .forms import group_form

# Create your views here.
def create_group(request):
    form = group_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("profile")
    context= {"form": form}
    return render(request, "groups/groups.html", context)

