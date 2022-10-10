from django.urls import path
from .views import create_group


urlpatterns = [
    path('create_group/', create_group, name = "groups"),

]