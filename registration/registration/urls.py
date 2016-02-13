from django.conf.urls import include, url
from django.contrib import admin
from regis.views import  OrganizationView, ParticipantsView 


urlpatterns = [

	url(r'^', OrganizationView.as_view(), name='home'),
	url(r'^admin/', include(admin.site.urls)),
   	url(r'^index/', include('regis.urls')),
   	# url(r'^thanks/$', 'regis.views.thankyou', name='thanks'),
    # url(r'^register/$', ParticipantsView.as_view(),name='register'),
  

]

