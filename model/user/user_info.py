#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from datetime import date
from dateutil.relativedelta import relativedelta
import random

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
        self.passwd = ""
        # date(YYYY, MM, dd)
        self.birthday = date.today()
        delta = relativedelta(self.birthday, date.today())
        self.age = delta.years
        self.sex = random.randomint(0, 1)