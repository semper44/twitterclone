from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Relationship
from groupapp.models import Groupapp
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# adding users to group once created
# @receiver(post_save, sender=User)
# def profile_create(sender, instance, created, **kwargs):
#     if created:
#         group= Group.objects.get(name = "members_group")
#         instance.groups.add(group)
        

@receiver(post_save, sender=Relationship)
def add_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    eg = instance
    if instance.status == "accept":
        print(eg)
        print("hy")
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()

# @receiver(post_save, sender=Relationship)
# def delete_friends(sender, instance, **kwargs):
#     user = Profile.objects.all()
#     user.friends.delete(user=instance)





