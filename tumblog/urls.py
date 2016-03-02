from django.conf.urls import url
from django.contrib import admin

from blog.views import list_posts


urlpatterns = [
    url(r'^blog/$', list_posts, name='list_posts'),
    url(r'^admin/', admin.site.urls),
]

