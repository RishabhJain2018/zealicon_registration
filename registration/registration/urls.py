from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'regis.views.administrator', name='base'),
	url(r'^index/$', 'regis.views.index', name='index'),
	url(r'^index/register/$','regis.views.participants_register', name='register'),
	url(r'^index/register/confirm/$', 'regis.views.confirm', name='confirm'),
	url(r'^index/register/confirm/print/$', 'regis.views.print_offline', name='print_offline'),

	url(r'^index/online/register/confirm/print/online/$', 'regis.views.print_online', name='print_online'),
	url(r'^index/search/$', 'regis.views.search', name='search'),
	url(r'^index/online/register$', 'regis.views.online_register', name='online_register'),
	url(r'^index/online/register/confirm$', 'regis.views.online_confirm', name='online_confirm'),
	
	url(r'^print/$','regis.views.print_id', name='print'),
	url(r'^print/receipt$', 'regis.views.print_receipt', name='print_receipt'),

	url(r'^view_record/$', 'regis.views.view_record', name='view_record'),

	url(r'^reset/$','regis.views.reset_counter', name='reset'),

	url(r'^custom/$', 'regis.views.custom', name='custom'),
	url(r'^logout/$', 'regis.views.logout', name='logout'),

]
