from django.db import models
from django.forms import ModelForm

import datetime
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 300)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __unicode__(self):
    	return self.title


class NewBlogForm(ModelForm):
    class Meta:
        model = Blog
    # title = forms.CharField(max_length = 300)
    # content = models.TextField()



# validation on a ModelForm

