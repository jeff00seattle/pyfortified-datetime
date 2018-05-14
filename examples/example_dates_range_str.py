#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from pprintpp import pprint
import datetime as dt
import pyfortified_datetime

start_dt = dt.date(2015, 12, 20)
end_dt = dt.date(2016, 1, 11)

print(type(pyfortified_datetime.dates_range(start_dt, end_dt)))

for dt in pyfortified_datetime.dates_range(start_dt, end_dt):
    pprint(dt.strftime("%Y-%m-%d"))

