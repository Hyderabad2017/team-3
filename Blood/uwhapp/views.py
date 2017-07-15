# -*- coding: utf-8 -*-
import urllib2
import cookielib
from getpass import getpass
import sys


from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponseBadRequest
from models import BloodBank, Donor, Event, RequestToDonor, DonorHistory
import cookielib,urllib2
from getpass import getpass
import sys

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

<<<<<<< HEAD
    def get_context_dict(self, blood_units):
=======
    def get_context_dict(self, blood_units, username):
>>>>>>> 387da88fcb245de7f7871d855a44a9351175c431
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
<<<<<<< HEAD
        list_donor = {'list_donor': list_donor, 'donor_requests': donor_request, 'blood_units': blood_units}
=======
        list_donor = {'list_donor': list_donor, 'donor_requests': donor_request, 'blood_units': blood_units,
                      'userid_bloodbank': username}
>>>>>>> 387da88fcb245de7f7871d855a44a9351175c431
        return list_donor

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        blood_bank_obj = BloodBank.objects.filter(userid=username)
        if len(blood_bank_obj) == 0:
            return redirect('/uwhapp/bloodbank')
        blood_bank_obj = blood_bank_obj[0]
        if blood_bank_obj.password == password:
<<<<<<< HEAD
            context = self.get_context_dict(blood_bank_obj.blood_units)
=======
            context = self.get_context_dict(blood_bank_obj.blood_units, username)
>>>>>>> 387da88fcb245de7f7871d855a44a9351175c431
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
<<<<<<< HEAD
        #login creds
        username = '8686342823'
        passwd = 'vamshi17'
        message = 'United Way of Hyderabad' 
        #Logging into the SMS Site
        url = 'http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
 
        #For Cookies:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
        # Adding Header detail:
        opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
 
=======
        # login creds
        username = '8686342823'
        passwd = 'vamshi17'
        message = 'United Way of Hyderabad'
        # Logging into the SMS Site
        url = 'http://site24.way2sms.com/Login1.action?'
        data = 'username=' + username + '&password=' + passwd + '&Submit=Sign+in'

        # For Cookies:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        # Adding Header detail:
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

>>>>>>> 387da88fcb245de7f7871d855a44a9351175c431
        try:
            usock = opener.open(url, data)
        except IOError:
            print("Error while logging in.")
            sys.exit(1)
<<<<<<< HEAD
 
 
        jession_id = str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+mobile+'&message='+message+'&msgLen=136'
        opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
            print("Error while sending message")
    
        sys.exit(1)




=======

        jession_id = str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token=' + jession_id + '&mobile=' + mobile + '&message=' + message + '&msgLen=136'
        opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url, send_sms_data)
        except IOError:
            print("Error while sending message")

        sys.exit(1)
>>>>>>> 387da88fcb245de7f7871d855a44a9351175c431

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
