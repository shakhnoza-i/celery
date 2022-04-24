from django.urls import path, include
from mainapp.views import test, send_mail_to_all

urlpatterns = [
    path('', test, name='test'),
    path('sendmail/', send_mail_to_all, name="sendmail"),
]