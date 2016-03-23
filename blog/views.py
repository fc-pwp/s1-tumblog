import requests
from requests_oauthlib import OAuth1

from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Post
from .models import Comment
from .models import Category
from .forms import PostEditForm
from .forms import CommentEditForm


#consumer_key = settings.SOCIAL_AUTH_TUMBLR_KEY
#consumer_secret = settings.SOCIAL_AUTH_TUMBLR_SECRET


def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentEditForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            if request.is_ajax():
                result_html = '<p>{pk} : {content}'.format(
                    pk=comment.pk,
                    content=comment.content,
                )
                return HttpResponse(result_html)
            else:
                return redirect('view_post', pk=post.pk)
    else:
        form = CommentEditForm()

    comments = Comment.objects.filter(post=post)

    return render(request, 'post_view.html', {
        'post': post,
        'comment_form': form,
        'comments': comments,
    })


@login_required
def create_post(request):
    tumblr = request.user.social_auth.filter(provider='tumblr').first()
    if not tumblr:
        raise Exception('Tumblr로 먼저 로그인을 하세요')
    oauth_key = tumblr.tokens['oauth_token']
    oauth_secret = tumblr.tokens['oauth_token_secret']
    url='http://api.tumblr.com/v2/blog/hannal/post'
    client = requests.Session()
    client.auth = OAuth1(consumer_key, consumer_secret, oauth_key, oauth_secret)

    if request.method == 'POST':
        form = PostEditForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            _params = {
                'title': post.title,
                'body': post.content,
                'type': 'text'
            }
            client.post(url, data=_params)
            return redirect('view_post', pk=post.pk)
    else:
        form = PostEditForm()

    return render(request, 'edit_post.html', {
        'form': form,
    })


def category_posts(request, category_pk):
    post_list = Post.objects.filter(category__pk=category_pk) \
                .order_by('-id')
    paginator = Paginator(post_list, 2)

    current_page = request.GET.get('page')

    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {
        'posts': posts,
    })


def list_posts(request, category_pk=None):
    if category_pk is None:
        post_list = Post.objects.all().order_by('-id')
    else:
        post_list = Post.objects.filter(category__pk=category_pk) \
                .order_by('-id')
    paginator = Paginator(post_list, 2)

    current_page = request.GET.get('page')

    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {
        'posts': posts,
    })


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentEditForm()

    return render(request, 'post_view.html', {
        'post': post,
        'comment_form': comment_form,
    })

