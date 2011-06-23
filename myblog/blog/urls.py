from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^$', 'blog.views.home'),
    url(r'^list$', 'blog.views.blog_list'),
    url(r'^search/(.*)$', 'blog.views.blog_search'),
    url(r'^editcomment/(?P<id>\d+)/?$','blog.views.comment_edit'),
    url(r'^(detail|info)/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.blog_detail'),
)
