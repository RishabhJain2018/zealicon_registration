from django.conf.urls import include, url


urlpatterns = [

	url(r'^my_profile/$', 'profiles.views.profile', name='profile'),

]
