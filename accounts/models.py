from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return "@{}".format(self.username)
