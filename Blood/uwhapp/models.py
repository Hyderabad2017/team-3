# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Donor(models.Model):
    blood_choices = (
        ('A+','a+'),
        ('B+','b+')
    )
    name = models.CharField(max_length=100)
    userid = models.CharField(primary_key=True,max_length=100)
    password = models.CharField(max_length=100)
    blood_type = models.CharField(choices=blood_choices , max_length=3)
    age = models.IntegerField()
    weight = models.FloatField()
    haemo = models.FloatField()
    last_donation = models.DateTimeField()
    #location is next

    def __str__(self):
        return self.name

class BloodBank(models.Model):
    name = models.CharField(max_length=200)
    userid = models.CharField(primary_key=True,max_length=200)
    password = models.CharField(max_length=200)
    #address is location of blood bank
    blood_units=models.IntegerField()

    def __str__(self):
        return self.name
