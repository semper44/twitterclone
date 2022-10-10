from django.urls import path
from .views import home_view, make_tweet_view, reply_view, post_list_view


urlpatterns = [
    path('home/', home_view),
    path('', home_view),
    path('create_tweet/', make_tweet_view, name="make-tweet"),
    path('reaction/', reply_view, name="reply"),
    path('post_list/<int:id>/', post_list_view, name="post_list"),
]
