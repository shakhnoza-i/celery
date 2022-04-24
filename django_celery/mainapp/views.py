from django.shortcuts import render
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

from mainapp.tasks import test_func, send_mail_func


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request): #(self, a, b)
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='mainapp.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    # name="schedule_mail_task_"+"5" - task name need to be unique
    # task='mainapp.tasks.send_mail_func' - same thing we do in celery.py file for another task
    return HttpResponse("Done")
