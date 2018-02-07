# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from userApp.models import UserDetail , Portfolio

# Register your models here.


class UserDetailAdmin(admin.ModelAdmin):
    list_display = [ user.name for user in UserDetail._meta.fields ]
    
admin.site.register(UserDetail, UserDetailAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = [ user.name for user in Portfolio._meta.fields ]

admin.site.register(Portfolio, PortfolioAdmin)
