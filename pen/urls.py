from django.conf.urls import patterns, include, url
from broadcast.views import broadcast_message 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^broadcast$', broadcast_message , name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
