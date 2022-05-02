from django.urls import path
from .views import home_view, make_tweet_view


urlpatterns = [
    path('tweets/<int:id>/', home_view),
    path('home/', make_tweet_view, name="home"),
]
