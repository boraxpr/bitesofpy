from datetime import date, timedelta


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    day = date(year=year, month=5, day=1)
    while 1:
        if day.weekday() == 6:
            day += timedelta(days=7)
            break
        day += timedelta(days=1)
    return day

# print(get_mothers_day_date(2014))
