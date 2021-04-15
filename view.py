#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eel
from view.eel import desktop

from model.user.user_info import UserInfo
from model.data.data_manager import DataManager
from controller import facebook
from controller import twitter
from controller.ten_minute import TenMinute
import settings

@eel.expose
def create_account(name_str:str):

    # Input Validation
    if len(name_str) == 0:
        return
    
    # Input string to list
    name_list = DataManager().str_to_list(name_str)

    ## process each item in list
    for name in name_list:

        # get temporary email
        tm = TenMinute()
        email = tm.get_temporary_mail()

        # make UserInfo
        user_info = UserInfo(name, email)

        result = twitter.create_account(user_info, tm)

        if result:
            print(user_info)



    

if __name__ == "__main__":
    desktop.start(settings.APP_NAME, settings.END_POINT, settings.SIZE)
