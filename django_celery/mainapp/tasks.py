
import requests
from datetime import datetime
from celery import shared_task
from django.contrib.auth import get_user_model # default user model
from django.core.mail import send_mail

from core import settings
from core.celery import app


"""celery does this task separately and we get result separately
improve user experience, users don't need to wait for any tasks to be
completed and after them get the response. So we can immediately get 
the response back
"""
# all work done by celery, in django we see only result
@shared_task(bind=True)
def test_func(self):
    for i in range(1, 10):
        print(i)
    return "done"


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email], # recipient email
            fail_silently=True, # if fails - it doesn't touch others
        )
    return "Done"
