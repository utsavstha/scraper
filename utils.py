import datetime
from calendar import monthrange
def add_days(date, number_of_days):
    return date + datetime.timedelta(days=number_of_days)

def add_months_to_date(start_date, months_to_add):
    year = start_date.year + (start_date.month + months_to_add - 1) // 12
    month = (start_date.month + months_to_add - 1) % 12 + 1
    day = start_date.day
    return datetime(year, month, day)

def get_number_of_days_in_month(year, month):
    _, end = monthrange(year, month)
    return end

def get_number_of_months():
    return 12


def get_number_of_days_in_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 366  # Leap year has 366 days
    else:
        return 365  # Regular year has 365 days