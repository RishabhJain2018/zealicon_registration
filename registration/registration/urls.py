from django.conf.urls import include, url
from django.contrib import admin
from regis.views import ParticipantsView, FeesView, OrganizationView


urlpatterns = [

   	url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', ParticipantsView.as_view(),name='register'),
    url(r'^fees/', FeesView.as_view(),name='fees'),
    url(r'^', OrganizationView.as_view(), name='home'),

]

