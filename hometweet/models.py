from django.db import models
from profiles.models import Profile


# Create your models here.
REACTION_CHIOCES = (
    ("like", "like"),
    ("love", "love"),
    ("angry", "angry"),
    ("care", "care"),
    ("wow", "wow"),
    ("sad", "sad"),
    )



class Post(models.Model):
    content = models.TextField()
    pics = models.ImageField(null= True, blank= True, upload_to= 'images/')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "tweet_author")

    def __str__(self):
        return f"{self.content}"
    

class Coment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "post_comments")
    comment_author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "comment_author")
    comments = models.TextField()
    comment_pics = models.ImageField(null= True, blank= True, upload_to= 'images/')
    comment_date_created = models.DateTimeField(auto_now_add=True)



class Reply(models.Model):
    reply_comments = models.ForeignKey(Coment, on_delete=models.CASCADE, related_name= "comment_reply")
    reply_author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "reply_author")
    reply = models.TextField()
    reply_pics = models.ImageField(null= True, blank= True, upload_to= 'images/')
    date_created = models.DateTimeField(auto_now_add=True)






class Reaction(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "profile")
    Reaction_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "post")
    Reaction_coment = models.ForeignKey(Coment,null=True, blank=True, on_delete=models.CASCADE, related_name= "coment")
    Reaction_reply = models.ForeignKey(Reply, null=True, blank=True, on_delete=models.CASCADE, related_name= "reaction_reply")
    reactions = models.CharField(max_length=50, choices=REACTION_CHIOCES)

    def __str__(self):
        return self.reactions



    
  
 