# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Stock , StockValue

class StockAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Stock._meta.fields]
admin.site.register(Stock,StockAdmin)

class StockValueAdmin(admin.ModelAdmin):
	list_display = [f.name for f in StockValue._meta.fields]
admin.site.register(StockValue,StockValueAdmin)