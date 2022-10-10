from unicodedata import name
from urllib import request
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver 
from .models import Groupapp,GroupappRelationship
from django.contrib.auth.models import Group, User

@receiver(m2m_changed , sender=Groupapp.members.through)
def members_group_add(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        print(args, kwargs)
        group= Group.objects.get(name = "group-private")
        instance.groups.add(group)
        

@receiver(post_save , sender=GroupappRelationship)
def members_group_add(sender, instance, created, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    member = Groupapp.objects.get(name= "ui")
    mem = member.members.all()
    if instance.status == "accept":
        member.members.add(sender)
        member.members.add(receiver)

@receiver(post_save , sender=GroupappRelationship)
def members_group_add(sender, instance, created, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    admins = Groupapp.objects.get(name = "ui")
    administrators = admins.admin.all()
    if instance.status == "accept":
        groups= Group.objects.get(name = "group-private")
        if sender not in administrators:
            sender.group.add(groups)
        elif receiver not in administrators:
            receiver.group.add(groups)
        

    variable = 1  
       

@receiver(post_save, sender=Groupapp)
def profile_create(sender, instance, created, **kwargs):
    if instance.admin:
        print("hy")
        # member= Groupapp.objects.get(name = "ui")
        # admin  = instance.admin
        # print(admin)
        # groups= Group.objects.get(name = "group-admins")
        # admin.profile.add(groups)
    
        
        
