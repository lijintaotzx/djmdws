# coding=utf-8
import time

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from tools.file_writer import FileWriter


class TimeoutChecker(MiddlewareMixin):
    def process_request(self, request):
        request.META['start_time'] = time.time()

    def process_response(self, request, response):
        start_time = request.META.get('start_time')
        end_time = time.time()
        if end_time - start_time > settings.VIEW_TIMEOUT_TIME:
            f = FileWriter('TIMEOUT_URL')
            f.write(request.path_info)

        return response
