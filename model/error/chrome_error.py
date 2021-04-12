#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ChromeElementCountError(Error):
    """Raised when the element count does not match"""
    pass