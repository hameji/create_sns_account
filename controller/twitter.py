#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import datetime

from model.chrome import driver_manager
from model.user.user_info import UserInfo

TOP = "https://twitter.com/?lang=ja"

class Twitter(object):

# _/_/_/_/_/_/_/_/_/_/_/_/_/
# Basic functions
# _/_/_/_/_/_/_/_/_/_/_/_/_/

    def __init__(self, user_info=None, tm=None):
        print("[Twitter] init")
        self.driver_manager = None
        self.user_info = user_info
        self.tm = tm

    def start(self):
        if self.driver_manager is None:
            print("[twitter] driver start")
            self.driver_manager = driver_manager.DriverManager()
            self.driver_manager.start_driver(False)

    def open_top(self):
        self.driver_manager.open_page(TOP)

    def __del__(self):
        print("[twitter] delete")
        self.driver_manager.__del__()

# _/_/_/_/_/_/_/_/_/_/_/_/_/
# Register functions
# _/_/_/_/_/_/_/_/_/_/_/_/_/ -- Page1

    def move_to_register_page(self): 
        """Move from top page to register page"""
        xpath = "//a[@href='/i/flow/signup']" 
        self.driver_manager.click_element(xpath, 0)

    def change_to_email(self): 
        """change tel to email"""
        xpath = "//div[contains(@role, 'button') and contains(@dir, 'auto') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, 0)

    def set_fullname(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'name')]"
        self.driver_manager.set_input(xpath, 0, self.user_info.fullname)

    # def clear_email(self):
    #     xpath = "//input[contains(@type, 'email') and contains(@name, 'email')]"
    #     self.driver_manager.clear_input(xpath, 0)

    def set_email(self):
        xpath = "//input[contains(@type, 'email') and contains(@name, 'email')]"
        self.driver_manager.set_input(xpath, 0,  self.user_info.email)

    def set_birthday(self):
        month_xpath = "//select[@id='月']"
        day_xpath = "//select[@id='日']"
        year_xpath = "//select[@id='年']"
        month_index = random.randint(1, 12) # self.user_info.birthday.month
        day_index = random.randint(1, 27) # self.user_info.birthday.day
        year_index = random.randint(19, 65) # datetime.date().year - self.user_info.birthday.year
        self.driver_manager.select_option(month_xpath, 0, month_index)
        self.driver_manager.select_option(day_xpath, 0, day_index)
        self.driver_manager.select_option(year_xpath, 0, year_index)

    def press_next_button1(self):
        xpath = "//div[contains(@role, 'button') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, 0)

    def set_user_info(self):
        """First, set user info"""
        self.set_fullname()
        self.set_email()
        self.set_birthday()

    def press_next_button2(self):
        xpath = "//div[contains(@role, 'button') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, 1)

    def press_register_button(self):
        xpath = "//div[contains(@role, 'button') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, -1)

    def set_code(self, code: str):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'verfication_code')]"
        self.driver_manager.set_input(xpath, 0,  code)

    # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

    def set_password(self):
        xpath = "//input[contains(@type, 'password') and contains(@name, 'password')]"
        self.driver_manager.set_input(xpath, 0,  self.user_info.passwd)

    def confirm(self):
        xpath = "//div[contains(@role, 'button') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, 0)
        ## https://twitter.com/i/flow/signup

    def press_not_now(self):
        xpath = "//div[contains(@role, 'button') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, 0)

    def notice_not_now(self):
        xpath = "//div[contains(@role, 'button') and contains(@tabindex, '0')]"
        self.driver_manager.click_element(xpath, 1)

# _/_/_/_/_/_/_/_/_/_/_/_/_/ -- Page2

    def set_confirmation_code(self, code: str):
        xpath = "//input[contains(@type, 'text') and contains(@id, 'code_in_cliff')]"
        self.driver_manager.set_input(xpath, 0, code)

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

def create_account(user_info: UserInfo, tm):
    """Automatically handles registration of a random account with input name.

    Args:
        fullName (str): The name of the new account

    Returns:
        user_info: Return templates with characters in templates.
    """
    print("[twitter] create_account")

    twitter = Twitter(user_info, tm)
    twitter.start()
    twitter.open_top()

    twitter.move_to_register_page()

    # 1/5 page
    twitter.change_to_email()
    twitter.set_user_info()
    twitter.press_next_button1()

    # 2/5 page
    twitter.press_next_button2()

    # 3/5 page
    twitter.press_register_button()

    # verification
    code = tm.wait_for_code()
    print(" ... code is: ", code)
    twitter.set_code(code)
    twitter.press_next_button2()

    # set password
    twitter.set_password()
    twitter.confirm()

    # setup account
    for i in range(4):
        twitter.press_not_now()
        # [settings] pic, introduction, topic, follow
    twitter.notice_not_now()
    # [settings] notice 

    return True

# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()