from django.conf import settings
from django.db import models
from django.utils import timezone

# generally, each model maps to a single database table
# in this first line we are defining our object 
# post is the name of our model
# each python model subclasses django.db.models.Model
class Post(models.Model):
  # these are the fields that we want in our model/database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


#this is a method - publish is the name of the method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
      # this method returns the Post title
        return self.title