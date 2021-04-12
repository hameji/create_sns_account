#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
from dataclasses import dataclass

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
        next_name_component = name_component.split("　")
        if has_full_width_char:
            self.firstname = next_name_component[1]
            self.lastname = next_name_component[0]
        else:
            self.firstname = next_name_component[0]
            self.lastname = next_name_component[1]