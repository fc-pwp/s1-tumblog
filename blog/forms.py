from django import forms

from .models import Post
from .models import Comment


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'is_published', 'content']
        # fields = '__all__'

