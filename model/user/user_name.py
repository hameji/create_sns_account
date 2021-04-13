#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
from dataclasses import dataclass

from model.error.user_error import NameDivisionError

@dataclass
class UserName(object):
    fullname: str
    firstname: str
    lastname: str

    def __init__(self, fullname: str):
        self.fullname = fullname
        has_full_width_char = False
        for char in fullname:
            if unicodedata.east_asian_width(char) == "F":
                has_full_width_char = True
            elif unicodedata.east_asian_width(char) == "W":
                has_full_width_char = True
        name_component = fullname.split(" ")
        total_name_split = []
        if len(name_component) == 1:
            total_name_split = name_component[0].split("　")
        else:
            for name in name_component:
                temp_name_split = name.split("　")
                total_name_split.append(temp_name_split)
        if len(total_name_split) != 2:
            raise NameDivisionError
        if has_full_width_char:
            self.firstname = total_name_split[1]
            self.lastname = total_name_split[0]
        else:
            self.firstname = total_name_split[0]
            self.lastname = total_name_split[1]
