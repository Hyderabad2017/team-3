# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponseBadRequest
from models import BloodBank, Donor, Event, RequestToDonor, DonorHistory


# Create your views here.
class Counter:
    counter = 0

    def increment(self):
        self.counter += 1
    def set_to_zero(self):
        self.counter = 0

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
    def donor_requests(self):
        donorRequests = RequestToDonor.objects.all()
        request_list = []
        for each_request in donorRequests:
            request_dict = {
                'name': each_request.requestee.name,
                'userid': each_request.requestee.userid,
                'request_units': each_request.request_date,
                'blood_bank': each_request.blood_banks.name
            }
            request_list.append(request_dict)
        return request_list

    def get_context_dict(self, blood_units):
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
            donor_request = self.donor_requests()
        list_donor = {'list_donor': list_donor, 'donor_requests': donor_request, 'blood_units': blood_units}
        return list_donor

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        blood_bank_obj = BloodBank.objects.filter(userid=username)
        if len(blood_bank_obj) == 0:
            return redirect('/uwhapp/bloodbank')
        blood_bank_obj = blood_bank_obj[0]
        if blood_bank_obj.password == password:
            context = self.get_context_dict(blood_bank_obj.blood_units)
            return render(request, 'uwhapp/bloodbank.html', context)
        else:
            return redirect('/uwhapp/bloodbank')


class DonorLogincheck(View):
    def get_context_dict(self, username):
        donor = Donor.objects.get(userid=username)
        context = {
            'name': donor.name,
            'last_donation': donor.last_donation
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
        context['events'] = events_list
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
            context['counter']=Counter()
            return render(request, 'uwhapp/donor.html', context)
        else:
            return redirect('/uwhapp/donor')


class DonorRegister(View):
    def post(self, request):
        return render(request, 'uwhapp/donor_register.html')


class RegisterDetailsOfDonor(View):
    def post(self, request):
        last_donated = request.POST['last_donated']
        if last_donated == '':
            last_donated = datetime.date.today() - datetime.timedelta(3 * 365 / 12)
        Donor.objects.create(
            name=request.POST['user'],
            userid=request.POST['userid'],
            password=request.POST['pass'],
            blood_type=request.POST['blood_type'],
            age=int(request.POST['age']),
            weight=int(request.POST['weight']),
            haemo=float(request.POST['haemo']),
            last_donation=last_donated,
            mobile=request.POST['mobile']
        )
        return render(request, 'uwhapp/success.html')


class SendAlert(View):
    def send_sms_request(self, mobile):
        pass

    def post(self, request):
        all_donor = Donor.objects.all()
        blood_bank = BloodBank.objects.get(name=request.POST.get('name'))
        for each_donor in all_donor:
            self.send_sms_request(each_donor.mobile)
            RequestToDonor.objects.create(
                requestee=each_donor,
                request_units=5,
                blood_bank=blood_bank
            )
        return render(request, 'uwhapp/success_request.html')


class DonationAccept(View):
    def send_thank_sms(self, userid):
        user_object = Donor.objects.get(userid=userid)
        mobile = user_object.mobile
        pass

    def post(self, request):
        userid = request.POST.get('userid')
        print userid
        request_donor_objects = RequestToDonor.objects.all()
        for each_request_to_donor in request_donor_objects:
            if each_request_to_donor.requestee.userid == userid:
                each_request_to_donor.delete()
        user_object = Donor.objects.get(userid=userid)
        DonorHistory.objects.create(
            date=datetime.datetime.now(),
            donor=user_object
        )
        self.send_thank_sms(userid)
