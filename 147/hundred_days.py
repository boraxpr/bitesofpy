from datetime import date

from dateutil.relativedelta import relativedelta

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    hundred_weekdays = list()
    while len(hundred_weekdays) < 100:
        if start_date.weekday() not in [5, 6]:
            hundred_weekdays.append(start_date)
        start_date += relativedelta(days=1)
    return hundred_weekdays



