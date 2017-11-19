# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class UserDetail(models.Model):
    username = models.CharField(max_length = 30, unique = True, primary_key = True)
    cash = models.FloatField(blank = False, null = False)
    stepCount = models.IntegerField(blank = False, null = False)

    class Meta:
        ordering = ('username', )
        default_related_name = 'userDetail'