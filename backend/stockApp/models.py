# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    info = models.CharField(max_length = 1000000000, default='')
   
    def __unicode__(self):
		return "%s"%(self.name)