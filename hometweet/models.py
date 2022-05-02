from django.db import models
from profiles.models import Profile


# Create your models here.
class Tweet(models.Model):
    content = models.TextField()
    pics = models.ImageField(null= True, blank= True, upload_to= 'images/')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "author")

    def __str__(self):
        return f"{self.content}-{self.author}"

  
 