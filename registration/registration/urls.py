from django.conf.urls import include, url
from django.contrib import admin
from regis.views import  OrganizationView, ParticipantsView 


urlpatterns = [

   	url(r'^admin/', include(admin.site.urls)),
   	url(r'^register.fees/receipt/$','regis.views.receipts', name='receipt'),
    url(r'^register/$', ParticipantsView.as_view(),name='register'),
    url(r'^', OrganizationView.as_view(), name='home'),

]

