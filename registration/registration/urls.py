from django.conf.urls import include, url
from django.contrib import admin
from regis.views import ParticipantsView, FeesView, OrganizationView


urlpatterns = [

   	url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', ParticipantsView.as_view(),name='home'),
    url(r'^fees/', FeesView.as_view(),name='fees'),
    url(r'^', OrganizationView.as_view()),

]