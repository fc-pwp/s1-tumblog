from django.conf.urls import url
from django.contrib import admin

from blog.views import list_posts
from blog.views import view_post


urlpatterns = [
    url(r'^blog/posts/(?P<pk>[0-9]+)/$', view_post, name='view_post'),
    url(r'^blog/$', list_posts, name='list_posts'),
    url(r'^admin/', admin.site.urls),
]

