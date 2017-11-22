# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from userApp.models import UserDetail

# Register your models here.

class UserDetailAdmin(admin.ModelAdmin):
    listDisplay = { user.name for user in UserDetail._meta.fields }

admin.site.register(UserDetail, UserDetailAdmin)