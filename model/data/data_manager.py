#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

if os.name == "nt": #Windows
    NEW_LINE_CODE = "\r\n"
elif os.name == "posix": #Mac
    NEW_LINE_CODE = "\n"

class DataManager(object):

    def str_to_list(self, input: str):
        result = []
        if "," in input:
            result = input.split(",")
        elif "、" in input:
            result = input.split("、")
        elif NEW_LINE_CODE in input:
            result = input.split(NEW_LINE_CODE)
        else:
            result = [input]
        return result