from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from weblog import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weblog.views.home', name='home'),
    # url(r'^weblog/', include('weblog.foo.urls')),
    # url(r'^$', 'weblog-not-everyday.herokuapp.com', name = 'home'),
    url(r'^blogs/', include('blogs.urls', namespace = 'blogs')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) 
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
