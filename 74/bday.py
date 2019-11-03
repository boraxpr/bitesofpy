import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    d = date.weekday()
    return calendar.day_name[d]



# dt = date(1968, 9, 25)
# print(weekday_of_birth_date(dt))

