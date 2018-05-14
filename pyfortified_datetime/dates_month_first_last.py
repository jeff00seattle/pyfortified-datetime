#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import datetime as dt

# requires python-dateutil (http://labix.org/python-dateutil)
from dateutil.relativedelta import relativedelta

def dates_month_first_last(month_date, date_format="%Y-%m-%d"):
    if not (isinstance(month_date, str) or isinstance(month_date, dt.datetime) or isinstance(month_date, dt.date)):
        raise TypeError("Invalid date type: {0}".format(type(month_date)))

    _month_date = None
    if isinstance(month_date, str):
        _month_date = dt.datetime.strptime(date_string=month_date, format=date_format)
    elif isinstance(month_date, dt.datetime):
        _month_date = month_date.date()
    elif isinstance(month_date, dt.date):
        _month_date = month_date
    else:
        raise TypeError("Invalid date type: {0}".format(type(month_date)))

    month_last_date = _month_date + relativedelta(day=1, months=+1, days=-1)
    month_first_date = _month_date + relativedelta(day=1)
    return month_first_date, month_last_date