# coding=utf-8
from django.conf import settings
from django.core.cache import caches
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

cache = caches['access_check']


class AccessChecker(MiddlewareMixin):
    def check_black_list(self, addr):
        return True if cache.get('access_black_{}'.format(addr)) else False

    def set_access_info(self, addr):
        user_access = ''.join([settings.ACCRESS_CHECK_PREFIX, addr])
        cache_get = cache.get_or_set(user_access, 0, settings.ACCRESS_CHECK_INTERVAL)

        cache_get = int(cache_get) + 1
        if cache_get >= settings.ACCRESS_CHECK_COUNT:
            cache.set(
                'access_black_{}'.format(addr),
                1,
                settings.ACCESS_BLACKLIST_INTERVAL
            )
            return

        cache.set(user_access, cache_get, cache.ttl(user_access))

    def process_request(self, request):
        addr = request.META['REMOTE_ADDR']

        if self.check_black_list(addr):
            return HttpResponse('过分了哈！')

        self.set_access_info(addr)
