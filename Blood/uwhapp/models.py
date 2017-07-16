# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Donor(models.Model):
    blood_choices = (
        ('A+', 'a+'),
        ('B+', 'b+')
    )
    name = models.CharField(max_length=100)
    userid = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    blood_type = models.CharField(choices=blood_choices, max_length=3)
    age = models.IntegerField()
    weight = models.FloatField()
    haemo = models.FloatField()
    mobile = models.CharField(max_length=10, unique=True)
    last_donation = models.DateField()


    def __str__(self):
        return self.name


class BloodBank(models.Model):
    name = models.CharField(max_length=200)
    userid = models.CharField(primary_key=True, max_length=200)
    password = models.CharField(max_length=200)
    blood_units = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class RequestToDonor(models.Model):
    requestee = models.ForeignKey(Donor)
    request_units = models.IntegerField()
    blood_bank = models.ForeignKey(BloodBank)


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_details = models.CharField(max_length=200)
    event_date = models.DateTimeField()


class DonorHistory(models.Model):
    date = models.DateField()
    donor = models.ForeignKey(Donor)


