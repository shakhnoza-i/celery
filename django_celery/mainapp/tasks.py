
import requests
from datetime import datetime, timedelta
from celery import shared_task, chain, group, chord
from django.contrib.auth import get_user_model # default user model
from django.core.mail import send_mail
from django.utils import timezone

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
def send_mail_func(self): # send mail to all users
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time) + timedelta(days=2) - convert datetime field to our local timezone
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "Email message body"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email], # recipient email
            fail_silently=True, # if fails - it doesn't touch others
        )
    return "Done"


@app.task
def add(x, y):
    return x + y

# When we chain tasks together, the second task will take the results of the first task as its first argument
res = chain(add.s(1, 2), add.s(3)).apply_async()


# Groups are used to execute tasks in parallel. The group function takes in a list of signatures.
job = group([add.s(2, 2), add.s(4, 4),])
result = job.apply_async()
result.ready()  # have all subtasks completed?
result.successful() # were all subtasks successful?
result.get() # [4, 8 ]



