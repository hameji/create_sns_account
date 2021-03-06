#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from dateutil.relativedelta import relativedelta
from dataclasses import dataclass
import random

from model.extension.string_extension import StringExtension
# from model.utils.datetime_utils import DatetimeUtils
from model.user.user_name import UserName

@dataclass
class UserInfo(UserName):
    fullname: str
    lastname: str
    firstname: str
    email: str
    passwd: str
    # birthday: datetime
    # age: int
    sex: int

    def __init__(self, full_name: str, e_mail: str):
        super().__init__(full_name)
        self.email = e_mail
        self.passwd = StringExtension().random(10)
        # random_birthday = DatetimeUtils().get_radom_date_for_age(18, 65)
        # print(random_birthday)
        # self.birthday = random_birthday
        # delta = relativedelta(self.birthday, datetime.today())
        # self.age = delta.years
        self.sex = random.randint(0, 1)

    def refresh_email(self, e_mail: str):
        self.email = e_mail
        return self

    def convert_to_list(self):
        return [self.fullname, self.email, self.passwd]