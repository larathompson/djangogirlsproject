from django.shortcuts import render

# Create your views here.
def post_list(request):
  #this returns the value it gets from calling another functoin called render
  return render(request, 'blog/post_list.html', {})