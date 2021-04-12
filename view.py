#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eel
from view.eel import desktop
import settings

@eel.expose
def create_account(name_list:str):
    print("start create")
    print(name_list)

if __name__ == "__main__":
    desktop.start(settings.APP_NAME, settings.END_POINT, settings.SIZE)
