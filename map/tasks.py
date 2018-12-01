import re
from datetime import datetime

from celery import shared_task
from geolite2 import geolite2
from django.db import IntegrityError
from .models import FileModel, Coordinates

@shared_task
def processing(file_id):
    """
    Task to to process uploaded files in order to extract data to send it to map
    :param file_id: id of file stored locally
    :return: True or False
    """
    ap_log = FileModel.objects.get(id=file_id)
    log_file = ap_log.log_file.path
    patt = re.compile('\[(.*)\]')
    for line in open(log_file):
        time_logged = datetime.strptime(patt.search(line).group(1), '%d/%b/%Y:%H:%M:%S %z')
        geo_reader = geolite2.reader()
        ip = line.split()[0]
        ip_info = geo_reader.get(ip)
        if ip_info and 'location' in ip_info.keys():
            long = ip_info['location']['longitude']
            lat = ip_info['location']['latitude']
            try:
                ip_save = Coordinates.objects.create(ip=ip, longitude=long,latitude=lat, time_logged=time_logged)
                ip_save.save()
            except IntegrityError:
                continue
    ap_log.processed = True
    ap_log.save()
    return True