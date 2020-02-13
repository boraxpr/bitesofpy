from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    while True:
        start_date += timedelta(days=num_days)
        biteperday = 0
        while biteperday < num_bites:
            biteperday += 1
            yield start_date

