# coding=utf-8
import random
import time

from django.conf import settings
from django.http import HttpResponse


# Create your views here.

def timeout_checker(request):
    time.sleep(random.choice([0, settings.VIEW_TIMEOUT_TIME + 0.1]))
    return HttpResponse('test is ok!')
