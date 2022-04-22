
import requests
from datetime import datetime
from celery import shared_task

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
