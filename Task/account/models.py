# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save	

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User)

def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
