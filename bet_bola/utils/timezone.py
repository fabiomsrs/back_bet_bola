import pytz
from datetime import datetime
import functools
from django.conf import settings

@functools.lru_cache()
def get_timezone():
    return pytz.timezone(settings.TIME_ZONE_LOCAL)

def now():
    timezone = get_timezone()
    return datetime.now(timezone)
