from django.conf.urls import include, url
from django.contrib import admin
from regis.views import RegisterView, FeesView

urlpatterns = [
    # Examples:
    # url(r'^$', 'registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', RegisterView.as_view()),
    url(r'^fees/', FeesView.as_view()),
]
