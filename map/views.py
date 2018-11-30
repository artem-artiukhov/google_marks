from django.shortcuts import render
# import requests
import json
import re

from datetime import datetime
# Create your views here.
from django.views.generic import ListView, FormView
from django.db import IntegrityError
from django import http
from django.core import serializers

from geolite2 import geolite2

from map.models import Coordinates
from map.forms import IPSendingForm


class CoordinateList(ListView):
    model = Coordinates
    context_object_name = 'context'
    template_name = 'map/ip_list.html'

    # def get(self, request, *args, **kwargs):
    #     return http.HttpResponse(serializers.serialize('json', self.model.objects.all()))


class CoordinatesForm(FormView):
    form_class = IPSendingForm
    template_name = 'map/upload.html'
    success_url = '/ips'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES['file_field']
        if form.is_valid():
            # reading single provided IP
            ip = form.cleaned_data['ip']
            if ip:
                geo_reader = geolite2.reader()
                ip_info = geo_reader.get(ip)
                long = ip_info['location']['longitude']
                lat = ip_info['location']['latitude']
                # time_logged =
                ip_save = Coordinates.objects.create(ip=ip, longitude=long,latitude=lat)
                ip_save.save()

            # working with uploaded file
            for i, line in enumerate(files):
                patt = re.compile('\[(.*)\]')
                # for i, line in enumerate(f):
                if i == 100:
                    break
                # print(i, line.decode('utf-8'))
                time_logged = datetime.strptime(patt.search(line.decode('utf-8')).group(1), '%d/%b/%Y:%H:%M:%S %z')
                geo_reader = geolite2.reader()
                ip = line.split()[0].decode('utf-8')
                ip_info = geo_reader.get(ip)
                long = ip_info['location']['longitude']
                lat = ip_info['location']['latitude']
                # time_logged =
                try:
                    ip_save = Coordinates.objects.create(ip=ip, longitude=long,latitude=lat, time_logged=time_logged)
                    ip_save.save()
                except IntegrityError:
                    continue
                # print(line.split()[0].decode('utf-8'), type(time_logged))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
    #     This method is called when valid form data has been POSTed.
    #     It should return an HttpResponse.
    #     form.send_email()
        return super().form_valid(form)

# with open('/home/aartiukhov/books/ip_long_lat', 'w') as out_file:
#     out_file.write('Item,IP,Longitude,Latitude')
# for i, ip in enumerate(open('/home/aartiukhov/books/ip.txt')):
#    if i == 100:
#        break
#    inform = json.loads(requests.get('http://api.ipstack.com/' + ip.strip() + '?access_key=f8ab99a004ca2d09f73c13bae2de75dc&format=1').text)
#    with open('/home/aartiukhov/books/ip_long_lat', 'a') as out_file:
#        out_file.write("{3:d},{0},{1:f},{2:f}\n".format(inform['ip'], inform['longitude'], inform['latitude'], i))