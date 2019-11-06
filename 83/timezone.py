from datetime import datetime

from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')
# naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aware_dt = utc.localize(naive_utc_dt)
    aus_dt = aware_dt.astimezone(AUSTRALIA)
    es_dt = aware_dt.astimezone(SPAIN)
    return aus_dt,es_dt


# aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)
# print(aus_dt.__str__() + " //////" + es_dt.__str__())
