#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eel
from view.eel import desktop

from model.user.user_name import UserName
from model.data.data_manager import DataManager
from controller import facebook
import settings

@eel.expose
def create_account(name_str:str):
    print(name_str)
    if len(name_str) == 0:
        return
    
    dM = DataManager()
    name_list = dM.str_to_list(name_str)
    print(name_list)

    for name in name_list:

        user_name = UserName(name)
        print(user_name)

    # facebook.create_account(name_list)

if __name__ == "__main__":
    desktop.start(settings.APP_NAME, settings.END_POINT, settings.SIZE)
