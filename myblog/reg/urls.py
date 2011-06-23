from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^login/$', 'reg.views.loginView'),
    url(r'^logout/$', 'reg.views.logoutView'),

)
