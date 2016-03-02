from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def list_posts(request):
    object_list = Post.objects.all().order_by('-created_at')
    ctx = {
        'posts': object_list,
    }
    return render(request, 'post_list.html', ctx)


def view_post(request, pk):
    the_post = Post.objects.get(pk=pk)
    ctx = {
        'post': the_post,
    }
    return render(request, 'post_view.html', ctx)

