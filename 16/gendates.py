from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    # born = PYBITES_BORN
    # count = 0
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)
        # if count != 3 and count != 8:
        #     yield born + timedelta(days=100)
        #     born += timedelta(days=100)
        # elif count == 3:
        #     yield PYBITES_BORN + timedelta(days=365)
        # elif count == 8:
        #     yield PYBITES_BORN + timedelta(days=365*2)
        # count += 1


# dates = list(islice(gen_special_pybites_dates(), 10))
# for date in dates:
#     print(date)
# print(PYBITES_BORN+timedelta(days=365*2))