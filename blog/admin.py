from django.contrib import admin

# Register your models here.
from .models import Post

#this makes the model visible on the admin page 
admin.site.register(Post)