from django.conf.urls import include, url
from django.contrib import admin
from regis.views import  OrganizationView, FeesView, ParticipantsView 


urlpatterns = [

   	url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', ParticipantsView.as_view(),name='register'),
    url(r'^register/fees/$', FeesView.as_view(),name='fees'),
    url(r'^', OrganizationView.as_view(), name='home'),

]

