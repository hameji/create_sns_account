#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.user.user_info import UserInfo
import eel
from view.eel import desktop

from model.user.user_name import UserName
from model.data.data_manager import DataManager
from controller import facebook
import settings

@eel.expose
def create_account(name_str:str):

    # Input Validation
    if len(name_str) == 0:
        return
    
    # Input string to list
    dM = DataManager()
    name_list = dM.str_to_list(name_str)

    ## process each item in list
    for name in name_list:

        user_info = UserInfo(name, "email@email.com")
        print(user_info)

        # facebook.create_account(user_info)

    

if __name__ == "__main__":
    desktop.start(settings.APP_NAME, settings.END_POINT, settings.SIZE)
