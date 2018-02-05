# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

class UserDetail(models.Model):
    username = models.CharField(max_length = 30, unique = True)
    cash = models.FloatField(blank = False, null = False)
    stepCount = models.IntegerField(blank = False, null = False)
    class Meta:
        ordering = ('username', )
        default_related_name = 'userDetail'

    def __str__(self):
        return "%s"%(self.username)

class Portfolio(models.Model):
    username = models.ForeignKey(UserDetail , on_delete = models.CASCADE)
    symbol = models.CharField(max_length = 10)
    volume = models.IntegerField(blank=True, null = True)
    averagePrice = models.FloatField(blank=True, null = True)

    class Meta:
        ordering = ('username', 'symbol', )
        default_related_name = 'portfolio'

    def __str__(self):
        return "%s"%(self.username)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
