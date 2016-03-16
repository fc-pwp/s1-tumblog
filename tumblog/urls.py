from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

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
        r'^login/$',
        login,
        {'template_name': 'login.html'},
        name='login_url'
    ),
    url(
        r'^logout/$',
        logout,
        {'next_page': '/login/'},
        name='logout_url'
    ),

    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
