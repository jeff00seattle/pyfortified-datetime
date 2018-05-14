#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from pprintpp import pprint
import datetime as dt
import pyfortified_datetime

month_first_date, month_last_date = pyfortified_datetime.dates_month_first_last(dt.date(2016, 12, 20))
pprint(month_first_date)
pprint(month_last_date)

month_first_date, month_last_date = pyfortified_datetime.dates_month_first_last(dt.date(2016, 2, 3))
pprint(month_first_date)
pprint(month_last_date)

month_first_date, month_last_date = pyfortified_datetime.dates_month_first_last(dt.date(2017, 2, 3))
pprint(month_first_date)
pprint(month_last_date)
