from dateutil.relativedelta import relativedelta
from pandas import pandas as pd
import datetime

dates = [datetime.date(2019, 3, 30), datetime.date(2019, 3, 23), datetime.date(2019, 3, 9), datetime.date(2019, 3, 2),
         datetime.date(2019, 3, 28), datetime.date(2019, 3, 17)]


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    dat_month = dates[0].month
    dat_year = dates[0].year
    start = datetime.date(dat_year, dat_month, 1)
    end = start + relativedelta(months=1) - relativedelta(days=1)
    date_rng = pd.date_range(start, end, freq="D")
    return date_rng[date_rng.isin(dates) == 0]


# breakpoint()
get_missing_dates(dates)
