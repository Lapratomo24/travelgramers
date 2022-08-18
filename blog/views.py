from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post

# Create your views here.


class PostList(ListView):
    """
    Class to showcase posts on the main page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
