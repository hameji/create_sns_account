#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime
from dateutil import relativedelta

class DatetimeUtils(object):
    def get_radom_date_for_age(self, start_age: int, end_age: int):
        dt_now = datetime.datetime.now()
        start_date = dt_now + relativedelta.relativedelta(years= -start_age)
        end_date = dt_now + relativedelta.relativedelta(years= -end_age)
        random_time = random.uniform(start_date.timestamp(), end_date.timestamp())
        random_date = datetime.datetime.fromtimestamp(random_time)
        return random_date

# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
