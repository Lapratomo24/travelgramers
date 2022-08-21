from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Class to create a comment form
    """
    class Meta:
        """
        Class to display the fields to be displayed
        """
        model = Comment
        fields = ('body',)
