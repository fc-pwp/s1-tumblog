from django import forms

from blog.models import Post
from blog.models import Comment


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content']


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

