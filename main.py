from pyradios import RadioBrowser
from requests_cache import CachedSession
import datetime
from datetime import timedelta


expire_after = timedelta(days=3)
session = CachedSession(
    cache_name='cache',
    backend='sqlite',
    expire_after=expire_after)
rb = RadioBrowser(session=session)
rb.countries()