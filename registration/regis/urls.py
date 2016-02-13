from django.conf.urls import patterns, include, url
from regis.views import OrganizationView, ParticipantsView

urlpatterns = [

	url(r'^$', 'regis.views.index', name='index'),
	url(r'^register/$', ParticipantsView.as_view(), name='register'),
	url(r'^register/confirm/$', 'regis.views.confirm', name='confirm'),

	]