#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import secrets

class StringExtension(str):
    def random(self, digits: int):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        # 記号を含める場合
        # chars += '%&$#()'
        random_str: str = ''.join(secrets.choice(chars) for x in range(digits))
        return random_str
