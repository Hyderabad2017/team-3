# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *

class DonorModel(admin.ModelAdmin):
    pass

admin.site.register(Donor,DonorModel)

class BloodbankModel(admin.ModelAdmin):
    pass

admin.site.register(BloodBank,BloodbankModel)

class RequestModel(admin.ModelAdmin):
    pass

admin.site.register(Requests,RequestModel)

class EventModel(admin.ModelAdmin):
    pass

admin.site.register(Event,EventModel)