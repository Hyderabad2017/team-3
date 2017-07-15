# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponseBadRequest
from models import BloodBank,Donor


# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, 'uwhapp/index.html')


class Bloodbank(View):
    def get(self, request):
        return render(request, 'uwhapp/bloodbank_login.html')

class Donor(View):
    def get(self,request):
        return render(request,'uwhapp/donor_login.html')


class BloodbankLogincheck(View):
    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        blood_bank_obj = BloodBank.objects.filter(userid=username)
        if len(blood_bank_obj) == 0:
            return redirect('/uwhapp/bloodbank')
        blood_bank_obj = blood_bank_obj[0]
        if blood_bank_obj.password == password:
            return render(request, 'uwhapp/bloodbank.html')
        else:
            return redirect('/uwhapp/bloodbank')


class DonorLogincheck(View):
    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        blood_bank_obj = Donor.objects.filter(userid=username)
        if len(blood_bank_obj) == 0:
            return redirect('/uwhapp/donor')
        blood_bank_obj = blood_bank_obj[0]
        if blood_bank_obj.password == password:
            return render(request, 'uwhapp/donor.html')
        else:
            return redirect('/uwhapp/donor')
