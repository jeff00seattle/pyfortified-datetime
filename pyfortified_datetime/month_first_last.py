#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import datetime as dt

# requires python-dateutil (http://labix.org/python-dateutil)
from dateutil.relativedelta import relativedelta

def month_first_last_dates(month_date, date_format="%Y-%m-%d"):
    """
    For a date 'date' returns the start and end date for the month of 'date'.
    Month with 31 days:
    >>> date = dt.date(2011, 7, 27)
    >>> month_day_range(date)
    (datetime.date(2011, 7, 1), datetime.date(2011, 7, 31))
    Month with 28 days:
    >>> date = dt.date(2011, 2, 15)
    >>> month_day_range(date)
    (datetime.date(2011, 2, 1), datetime.date(2011, 2, 28))
    """
    if not (isinstance(month_date, str) or isinstance(month_date, dt.datetime)):
        raise TypeError("Expects parameter 'month_date' either as type string or datetime")

    month_datetime = dt.datetime.strptime(date_string=month_date, format=date_format) if isinstance(month_date, str) else month_date

    month_last_datetime = month_datetime + relativedelta(day=1, months=+1, days=-1)
    month_first_datetime = month_datetime + relativedelta(day=1)
    return month_first_datetime, month_last_datetime