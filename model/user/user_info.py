#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
import date

@dataclass
class UserInfo(object):
    lastname: str
    firstname: str
    email: str
    passwd: str
    birthday: date
    age: int
    sex: int
