from django.shortcuts import render
from django.http import HttpResponse

from mainapp.tasks import test_func


def test(request):
    test_func.delay()
    return HttpResponse("Done")
