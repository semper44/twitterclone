from django.urls import path
from .views import (
    register_view,
    login_view,
    profile_view,
    view_friends,
    find_friends,
    remove_friend_view,
    add_friend_view,
    view_sent_request,
    logout_view,
    view_received_request,
    search_view,
    block_user_view
)




urlpatterns = [
    path('register/', register_view, name = "register"),
    path('login/', login_view, name = "login"),
    path('profile/', profile_view, name = "profile"),
    path('friends/', view_friends, name = "friends"),
    path('findfriends/', find_friends, name = "findfriends"),
    path('removefriends/<int:id>/', remove_friend_view, name = "removefriends"),
    path('addfriends/<int:id>/', add_friend_view, name = "addfriends"),
    path('viewsentrequest/', view_sent_request, name = "viewsentrequest"),
    path('received_request/', view_received_request, name = "view_received_request"),
    path('logout/', logout_view, name = "logout"),
    path('search/', search_view, name = "search"),
    path('blockuser/<int:id>/', block_user_view, name = "blockuser"),

]