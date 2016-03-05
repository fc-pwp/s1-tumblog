from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from .models import Post
from .models import Category
from .forms import PostEditForm


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


def create_post(request):
    if request.user.is_authenticated() is False:
        raise Exception('로그인 하세요')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_pk = request.POST.get('category')

        if not title or not category_pk or not content:
            raise Exception('제목과 카테고리와 본문은 필수')

        category = get_object_or_404(Category, pk=category_pk)
        new_post = Post()
        new_post.title = title
        new_post.content = content
        new_post.category = category
        new_post.user = request.user
        new_post.save()

        return redirect('view_post', pk=new_post.pk)

    elif request.method == 'GET':
        form = PostEditForm()
        categories = Category.objects.all()

    ctx = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'edit_post.html', ctx)

