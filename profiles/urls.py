from django.urls import path
from .views import (
    register_view,
    login_view,
    profile_view,
    view_friends,
    find_friends,
    remove_friend_view,
    add_friend_view
)




urlpatterns = [
    path('register/', register_view, name = "register"),
    path('login/', login_view, name = "login"),
    path('profile/', profile_view, name = "profile"),
    path('friends/', view_friends, name = "friends"),
    path('findfriends/', find_friends, name = "findfriends"),
    path('removefriends/', remove_friend_view, name = "removefriends"),
    path('addfriends/<int:id>/', add_friend_view, name = "addfriends"),

]