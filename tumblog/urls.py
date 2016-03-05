from django.conf.urls import url
from django.contrib import admin

from blog import views as blog_views


urlpatterns = [
    url(r'^blog/posts/edit/$', blog_views.create_post, name='create_post'),
    url(r'^blog/posts/(?P<pk>[0-9]+)/$', blog_views.view_post, name='view_post'),
    url(r'^blog/$', blog_views.list_posts, name='list_posts'),
    url(r'^admin/', admin.site.urls),
]

