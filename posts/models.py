from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from groups.models import Group
from django.utils import timezone
# Create your models here.
import misaka
# from django.contrib.auth.models import settings.AUTH_USER_MODEL
from django.conf import settings

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='posts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField()
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username,
                                                'pk':self.pk})

    class Meta:
        ordering =['-created_at']
        unique_together=['user','message']


class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    create_date=models.DateTimeField(auto_now=True)
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)

    def __str__(self):
        return self.author
