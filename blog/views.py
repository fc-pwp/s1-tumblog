from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from blog.models import Post


def list_posts(request):
    page = request.GET.get('page', 1)

    object_list = Post.objects.all().order_by('-created_at')
    per_page = 2
    pn = Paginator(object_list, per_page)

    try:
        posts = pn.page(page)
    except PageNotAnInteger:
        posts = pn.page(1)
    except EmptyPage:
        posts = pn.page(pn.num_pages)

    ctx = {
        'posts': posts,
    }
    return render(request, 'post_list.html', ctx)


def view_post(request, pk):
    the_post = get_object_or_404(Post, pk=pk)
    ctx = {
        'post': the_post,
    }
    return render(request, 'post_view.html', ctx)

