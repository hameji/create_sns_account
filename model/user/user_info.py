#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta
from dataclasses import dataclass
import random

from model.extension import string_extension

@dataclass
class UserInfo(object):
    lastname: str
    firstname: str
    email: str
    passwd: str
    birthday: date
    age: int
    sex: int

    def __init__(self, last_name: str, first_name: str, e_mail: str, start_age: int, end_age: int):
        self.lastname = last_name
        self.firstname = first_name
        self.email = e_mail
        self.passwd = string_extension.random(10)
        # date(YYYY, MM, dd)
        self.birthday = date.today()
        delta = relativedelta(self.birthday, date.today())
        self.age = delta.years
        self.sex = random.randomint(0, 1)

    def refresh_email(self, user_info):
        self.lastname = user_info.lastname
        self.firstname = user_info.first_name
        self.email = user_info.e_mail # todo: change to 10min email
        self.passwd = user_info.passwd
        self.birthday = user_info.birthday
        self.age = user_info.age
        self.sex = user_info.sex
        return self



