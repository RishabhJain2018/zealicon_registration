from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'regis.views.administrator', name='base'),
	url(r'^index/$', 'regis.views.index', name='index'),
	url(r'^index/register/$','regis.views.participants_register', name='register'),
	url(r'^index/register/confirm/$', 'regis.views.confirm', name='confirm'),
	url(r'^index/online/$', 'regis.views.online', name='online'),
	url(r'^search/$', 'regis.views.online_search'),

  

]

