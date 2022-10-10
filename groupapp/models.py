from pickle import TRUE
from statistics import mode
from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your models here.
  

class Groupapp(models.Model):
    groups = models.ManyToManyField(Group, blank= True, related_name="group")
    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    cover_photo = models.ImageField(null= True, blank=True, upload_to="images/")
    description = models.CharField(max_length=100, null=False, blank=False)
    members = models.ManyToManyField(Profile, related_name="members")
    admin = models.ManyToManyField(Profile, related_name="admin")
    videos = models.FileField(null= True, blank=True, upload_to="media/")
    images = models.ImageField(null= True, blank=True, upload_to="images/")
    text = models.TextField(null= True, blank=True)

    def __str__(self):
        return(self.name)

STATUS_CHOICES = (
    ("accept", "accept"),
    ("send", "send"),
    )

class GroupappRelationship(models.Model):
    groupapp = models.ManyToManyField(Groupapp, related_name="groupapps")
    sender = models.ForeignKey(Profile, on_delete= models.CASCADE,  related_name= "groupsenders")
    receiver = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name= 'groupreceivers')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

