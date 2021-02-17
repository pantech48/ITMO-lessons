from datetime import date, timedelta


def weekend_generator(start, end):
     while start < end:
        if 6 <= start.isoweekday() <= 7:
            yield start
        start += timedelta(days=1)













