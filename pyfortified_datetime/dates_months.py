#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

def dates_months_list(start_date, end_date, date_format="%Y-%m"):
    from dateutil.rrule import rrule, MONTHLY
    return [dt.strftime(date_format) for dt in rrule(MONTHLY, dtstart=start_date, until=end_date)]

def dates_months_generator(start_date, end_date, date_format="%Y-%m"):
    from dateutil.rrule import rrule, MONTHLY
    return (dt.strftime(date_format) for dt in rrule(MONTHLY, dtstart=start_date, until=end_date))