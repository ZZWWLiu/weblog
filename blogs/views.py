# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Blog
from django.core.cache import cache
import logging
import re
USER_RE     = re.compile(r"^[a-zA-Z0-9]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE    = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_username(name):
    return USER_RE.match(name)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_verify(verify,password):
    return verify == password

def valid_email(email):
    return email == '' or EMAIL_RE.match(email)

def homepage(request):
    key = 'top10'
    latest_blogs = cache.get(key)
    if latest_blogs is None:
        logging.error('hitting the DB!')
    	latest_blogs = Blog.objects.all().order_by('-created')[:10]
        cache.set(key, latest_blogs)
	context = {'latest_blogs': latest_blogs}
	return render(request, 'blogs/mainpage.html', context)

def permalink(request, blog_id):
    blog = cache.get(blog_id)
    if blog is None:
        blog = get_object_or_404(Blog, id = int(blog_id))
        cache.set(blog_id, blog)
	return render(request, 'blogs/permalink.html', {'blog':blog})



def postpage(request):
	if request.method == 'GET':
		return render(request, 'blogs/postnew.html')
	if request.method == 'POST':
		title   = request.POST['subject']
        content = request.POST['content']

        if title and content:
            blog = Blog(title = title, content=content)
            blog.save()
            # memcache.set("update", True)
            # cache = memcache.get("top10")
            # print "cached : ",cache
            # cache.insert(0, blog)
            # cache = cache[:10]
            # memcache.set("top10", cache)
            # memcache.delete("time")
            blog_id = blog.id
            return redirect('/blogs/%s' %str(blog_id))
            
        else:
            error = 'We need both a title and content'
            context = {'title': title,
                       'content': content,
                       'error': error
            }
            return render(request, 'blogs/postnew.html', context)

def signup(request):
    if request.method == 'GET':
        c = {}
        return render(request, 'blogs/signup.html',c)



