#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

def dates_range(date1, date2):
    import datetime as dt
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + dt.timedelta(n)