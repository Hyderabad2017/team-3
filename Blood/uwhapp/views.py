# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponseBadRequest
from models import BloodBank, Donor, Event


# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, 'uwhapp/index.html')


class Bloodbank(View):
    def post(self, request):
        return render(request, 'uwhapp/bloodbank_login.html')


class DonorPage(View):
    def post(self, request):
        return render(request, 'uwhapp/donor_login.html')


class BloodbankLogincheck(View):
    def get_context_dict(self):
        all_donors = Donor.objects.all()
        list_donor = []
        for each_donor in all_donors:
            each_context = {
                'name': each_donor.name,
                'blood_type': each_donor.blood_type,
                'age': each_donor.age,
                'haemo': each_donor.haemo,
                'last_donation': each_donor.last_donation
            }
            list_donor.append(each_context)
            list_donor = {'list_donor': list_donor}
        return list_donor

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        blood_bank_obj = BloodBank.objects.filter(userid=username)
        if len(blood_bank_obj) == 0:
            return redirect('/uwhapp/bloodbank')
        blood_bank_obj = blood_bank_obj[0]
        if blood_bank_obj.password == password:
            context = self.get_context_dict()
            return render(request, 'uwhapp/bloodbank.html', context)
        else:
            return redirect('/uwhapp/bloodbank')


class DonorLogincheck(View):
    def get_context_dict(self, username):
        donor = Donor.objects.get(userid=username)
        context = {
            'name': donor.name
        }
        events = Event.objects.all()
        events_list = []
        for each_event in events:
            event_dict = {
                'event_name': each_event.event_name,
                'event_details': each_event.event_details,
                'event_date': each_event.event_date
            }
            events_list.append(event_dict)
        context['event_details'] = events_list
        return context

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        blood_bank_obj = Donor.objects.filter(userid=username)
        if len(blood_bank_obj) == 0:
            return redirect('/uwhapp/donor')
        blood_bank_obj = blood_bank_obj[0]
        if blood_bank_obj.password == password:
            context = self.get_context_dict(username)
            return render(request, 'uwhapp/donor.html', context)
        else:
            return redirect('/uwhapp/donor')


class DonorRegister(View):
    def post(self, request):
        return render(request, 'uwhapp/donor_register.html')


class RegisterDetailsOfDonor(View):
    def post(self, request):
        Donor.objects.create(
            name=request.POST['name'],
            userid=request.POST['userid'],
            password=request.POST['pass'],
            blood_type=request.POST['blood_type'],
            age=int(request.POST['age']),
            weight=int(request.POST['weight']),
            haemo=float(request.POST['haemo']),
            last_donation=request.POST['last_donation'],
            mobile=request.POST['mobile']
        )
        return render(request, 'uwhapp/success.html')


class SendAlert(View):
    def post(self,request):
        all_donor = Donor.objects.all()
        for each_donor in all_donor:
            print each_donor
