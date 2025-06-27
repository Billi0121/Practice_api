from rest_framework import throttling
import datetime 
from rest_framework.exceptions import Throttled

class LowRequestRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 0 and now <= 3:
            raise Throttled(detail='Bro dont spam! Give us some rest!')
        return True