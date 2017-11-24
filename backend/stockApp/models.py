# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length = 20)
    fullname = models.CharField(max_length = 1000)
   
    def __unicode__(self):
		return "%s"%(self.name)

class StockValue(models.Model):
    name = models.ForeignKey(Stock , on_delete = models.CASCADE)
    date = models.DateField(blank=True)
    openPrice = models.FloatField(blank=True, null = True)
    closePrice = models.FloatField(blank=True, null = True)
    high = models.FloatField(blank=True, null = True)
    low = models.FloatField(blank=True, null = True)
    adjClose = models.FloatField(blank=True, null = True)
    volume = models.FloatField(blank=True, null = True)
   
    def __unicode__(self):
		return "%s"%(self.name)