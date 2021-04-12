#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import secrets

class String(str):
    def random(self, digits: int):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        # 記号を含める場合
        # chars += '%&$#()'
        random_str: str = ''.join(secrets.choice(chars) for x in range(digits))
        self = super().__new__(self, random_str)
        return self
