from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    prof_pics = models.ImageField(null = True, blank =True, upload_to= 'images/')
    friends = models.ManyToManyField(User, blank=True, related_name="friend" )
    bio = models.TextField(blank= True)
    # slug = models.SlugField(unique= True, blank= True)

    def __str__(self):
        return str(self.user)


STATUS_CHOICES = (
    ("accept", "accept"),
    ("send", "send"),

)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete= models.CASCADE, null= True, related_name= "senders")
    receiver = models.ForeignKey(Profile, on_delete= models.CASCADE, null= True, related_name= 'receivers')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"