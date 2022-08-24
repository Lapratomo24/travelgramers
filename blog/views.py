from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, ShareForm

# Create your views here.


class PostList(ListView):
    """
    Class to showcase posts on the main page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    Class to view the content of a selected post
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class PostLike(View):
    """
    Class to give users the ability to like or unlike posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Class to allow a logged-in user to add a new post
    """
    form_class = ShareForm
    template_name = 'create.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        Method to set the logged-in user as the author of a new post
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        Message to indicate a successfully-created new post
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )
