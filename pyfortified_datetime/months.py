#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

def months_list(start_datetime, end_datetime, date_format="%Y-%m"):
    from dateutil.rrule import rrule, MONTHLY
    return [dt.strftime(date_format) for dt in rrule(MONTHLY, dtstart=start_datetime, until=end_datetime)]

def months_generator(start_datetime, end_datetime, date_format="%Y-%m"):
    from dateutil.rrule import rrule, MONTHLY
    return (dt.strftime(date_format) for dt in rrule(MONTHLY, dtstart=start_datetime, until=end_datetime))