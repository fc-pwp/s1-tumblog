from django.contrib import admin

from blog.models import Post
from blog.models import Category
from blog.models import Comment
from blog.models import Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
