"""tumblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login

from blog import views as blog_views

urlpatterns = [
    url(r'^blog/posts/edit/$', blog_views.create_post, name='create_post'),
    url(r'^blog/$', blog_views.list_posts, name='list_posts'),
    url(
        r'^blog/category/(?P<category_pk>[0-9]+)/$',
        blog_views.list_posts, name='category_list_posts'
    ),
    url(r'^blog/(?P<pk>[0-9]+)/$', blog_views.view_post, name='view_post'),
    url(
        r'^blog/(?P<pk>[0-9]+)/comments/$', blog_views.create_comment,
        name='create_comment'
    ),
    url(
        r'^accounts/login/$',
        login,
        {'template_name': 'login.html'},
        name='login_url'
    ),
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
