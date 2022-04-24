from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core') # core - project name
app.conf.enable_utc = False # cause we use our own timezone
app.conf.update(timezone = 'Asia/Almaty')

app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    'send-mail-every-day-at-12am': {
        'task': 'mainapp.tasks.send_mail_func',
        'schedule': crontab(hour=0, minute=0, day_of_month=19, month_of_year = 6), # day_of_week
        # 'schedule': 15,
        #'args': (2,) - to pass any datastructure as arguments to send_mail_func()
    }
}
app.autodiscover_tasks(settings.INSTALLED_APPS)
