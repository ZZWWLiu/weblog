from django.conf.urls import patterns, url

from blogs import views


urlpatterns = patterns('',
	# ex: /blogs/
	url(r'^$', views.homepage, name = 'homepage'),
    # ex: /blogs/12
	url(r'^(?P<blog_id>\d+)/$', views.permalink, name = 'permalink'),
	# ex: /blogs/post
	url(r'^post', views.postpage, name = 'postpage'),
	# ex: /blogs/signup
	url(r'^signup', views.signup, name = 'signup'),
)