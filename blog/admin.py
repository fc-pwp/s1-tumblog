from django.contrib import admin

from blog.models import Post
from blog.models import Category 

admin.site.register(Post)
admin.site.register(Category)
