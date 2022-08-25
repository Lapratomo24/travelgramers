from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    Class to create a comment form
    """
    class Meta:
        """
        Class to display the comment field
        """
        model = Comment
        fields = ('body',)


class ShareForm(forms.ModelForm):
    """
    Class to create a form that users can fill out to share their
    travel experience
    """

    def __init__(self, *args, **kwargs):
        super(ShareForm, self).__init__(*args, **kwargs)

    class Meta:
        """
        Class to display the fields for users to fill out on the experience
        form page
        """
        model = Post
        fields = [
            "title",
            "featured_image",
            "status",
            "description",
            "attractions",
        ]

        widgets = {
            "description": SummernoteWidget(),
            "attractions": SummernoteWidget(),
        }



