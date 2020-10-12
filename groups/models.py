from django.db import models


from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
#import misaka
# from django.contrib.auth.models import settings.AUTH_USER_MODEL
from django.conf import settings

from django import template
register=template.Library()

class Group(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    description=models.TextField(blank=True,default='')
    members=models.ManyToManyField(settings.AUTH_USER_MODEL,through="Groupmember")

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering =['name']



class Groupmember(models.Model):
    group=models.ForeignKey(Group,related_name='membership',on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together=('group','user')
