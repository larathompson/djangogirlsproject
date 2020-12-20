from django.shortcuts import render
from django.utils import timezone
from .models import Post 

# Create your views here.
def post_list(request):
  #this returns the value it gets from calling another functoin called render
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # we are passing the posts in for the templates to use
    return render(request, 'blog/post_list.html', {'posts': posts})