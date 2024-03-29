.. -*- mode: rst -*-

pyfortified-datetime
-------------------

Important Note
^^^^^^^^^^^^^^

Work In Progress
^^^^^^^^^^^^^^^^

Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs| |license|
    * - package
      - |version| |supported-versions|

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |version| image:: https://img.shields.io/pypi/v/pyfortified_datetime.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pyfortified_datetime

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/logging-fortified.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/logging-fortified

.. end-badges


Install
-------

.. code-block:: bash

    pip install pyfortified-datetime


Functions
---------

.. code-block:: python

    import pyfortified_datetime
    import datetime as dt

    month_first_date, month_last_date = pyfortified_datetime.dates_month_first_last(dt.date(2016, 12, 20))
    print(month_first_date)
    print(month_last_date)

.. code-block:: bash

    datetime.date(2016, 12, 1)
    datetime.date(2016, 12, 31)


.. code-block:: python

    import pyfortified_datetime
    import datetime as dt

    start_dt = dt.date(2015, 12, 20)
    end_dt = dt.date(2016, 1, 6)

    for dt in pyfortified_datetime.dates_range(start_dt, end_dt):
        pprint(dt.strftime("%Y-%m-%d"))


.. code-block:: bash

    '2015-12-20'
    '2015-12-21'
    '2015-12-22'
    '2015-12-23'
    '2015-12-24'
    '2015-12-25'
    '2015-12-26'
    '2015-12-27'
    '2015-12-28'
    '2015-12-29'
    '2015-12-30'
    '2015-12-31'
    '2016-01-01'
    '2016-01-02'
    '2016-01-03'
    '2016-01-04'
    '2016-01-05'
    '2016-01-06'


.. code-block:: python

    import pyfortified_datetime
    import datetime as dt

    start_dt = dt.date(2016, 12, 20)
    end_dt = dt.date(2018, 1, 11))

    for dt in pyfortified_datetime.dates_months_list(start_dt, end_dt):
        print(dt)


.. code-block:: bash

    '2016-12'
    '2017-01'
    '2017-02'
    '2017-03'
    '2017-04'
    '2017-05'
    '2017-06'
    '2017-07'
    '2017-08'
    '2017-09'
    '2017-10'
    '2017-11'
    '2017-12'