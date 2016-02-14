from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = [

   	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'regis.views.Administrator',name='base'),
    url(r'^index/$', 'regis.views.index', name='index'),
    url(r'^index/register/$','regis.views.Participants', name='register'),
    url(r'^index/register/confirm/$','regis.views.Confirm', name='confirm'),
    url(r'^index/online/$', 'regis.views.Online', name='online'),
    url(r'^search/$', 'regis.views.Search', name='search'),

]

