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
from .forms import CommentEditForm


def create_comment(request, pk):
    if not request.user.is_authenticated():
        raise Exception('로그인을 하지 않았습니다')

    post = get_object_or_404(Post, pk=pk, is_published=True)
    form = CommentEditForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.user = request.user
        new_comment.save()
        return redirect('view_post', pk=post.pk)

    return render(request, 'post_view.html', {
        'post': post,
        'comment_form': form,
    })


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
    comment_form = CommentEditForm()
    ctx = {
        'post': the_post,
        'comment_form': comment_form,
    }
    return render(request, 'post_view.html', ctx)


def create_post(request):
    if request.user.is_authenticated() is False:
        raise Exception('로그인 하세요')

    categories = Category.objects.all()

    if request.method == 'POST':
        form = PostEditForm(request.POST)
        if form.is_valid():
            # category = get_object_or_404(Category, pk=category_pk)
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('view_post', pk=new_post.pk)

    elif request.method == 'GET':
        form = PostEditForm()

    ctx = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'edit_post.html', ctx)

