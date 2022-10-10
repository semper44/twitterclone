from cgitb import lookup
from multiprocessing import Manager
from unittest import result
from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver


# Create your models here.
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    prof_pics = models.ImageField(null = True, blank =True, upload_to= 'images/')
    friends = models.ManyToManyField(User, blank=True, related_name="friend" )
    bio = models.TextField(blank= True)
    group = models.ManyToManyField(Group, blank=True,)
    # slug = models.SlugField(unique= True, blank= True)


    def __str__(self):
        return str(self.user)

    
    class Meta:
        permissions = [("cant_view_profile","cant view profile")]





    
STATUS_CHOICES = (
    ("accept", "accept"),
    ("send", "send"),

)

        
class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete= models.CASCADE,  related_name= "senders")
    receiver = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name= 'receivers')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

class blockedusers(models.Model):
    blocker = models.ForeignKey(Profile, on_delete= models.CASCADE,  related_name= "blocker")
    blocked = models.ForeignKey(Profile, on_delete= models.CASCADE,  related_name= "blocked")