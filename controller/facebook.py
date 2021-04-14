#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import datetime

from model.chrome import driver_manager
from model.user.user_info import UserInfo

TOP = "https://www.facebook.com/"
EMAIL_CONFIRM_PARTIAL_URL = "https://www.facebook.com/confirmemail.php?next="

class Facebook(object):

# _/_/_/_/_/_/_/_/_/_/_/_/_/
# Basic functions
# _/_/_/_/_/_/_/_/_/_/_/_/_/

    def __init__(self, user_info=None, tm=None):
        print("[Facebook] init")
        self.driver_manager = None
        self.user_info = user_info
        self.tm = tm

    def start(self):
        if self.driver_manager is None:
            print("start")
            self.driver_manager = driver_manager.DriverManager()
            self.driver_manager.start_driver()

    def open_top(self):
        self.driver_manager.open_page(TOP)

    # def __del__(self):
    #     self.driver_manager.__del__()

# _/_/_/_/_/_/_/_/_/_/_/_/_/
# Register functions
# _/_/_/_/_/_/_/_/_/_/_/_/_/ -- Page1

    def move_to_register_page(self): 
        """Move from top page to register page"""
        xpath = "//a[contains(@role, 'button') and contains(text(), '新しいアカウントを作成')]" 
        self.driver_manager.click_element(xpath, 0)

    def set_lastname(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'lastname')]"
        self.driver_manager.set_input(xpath, 0, self.user_info.lastname)

    def set_firstname(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'firstname')]"
        self.driver_manager.set_input(xpath, 0, self.user_info.firstname)

    def clear_email(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'reg_email__')]"
        self.driver_manager.clear_input(xpath, 0)

    def set_email(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'reg_email__')]"
        self.driver_manager.set_input(xpath, 0,  self.user_info.email)

    def clear_confirm_email(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'reg_email_confirmation__')]"
        self.driver_manager.clear_input(xpath, 0)

    def set_confirm_email(self):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'reg_email_confirmation__')]"
        self.driver_manager.set_input(xpath, 0,  self.user_info.email)

    def set_password(self):
        xpath = "//input[contains(@type, 'password') and contains(@name, 'reg_passwd__')]"
        self.driver_manager.set_input(xpath, 0,  self.user_info.passwd)

    def set_birthday(self):
        year_xpath = "//select[@id='year']"
        month_xpath = "//select[@id='month']"
        day_xpath = "//select[@id='day']"
        year_index = random.randint(18, 65) # datetime.date().year - self.user_info.birthday.year
        month_index = random.randint(0, 11) # self.user_info.birthday.month
        day_index = random.randint(0, 27) # self.user_info.birthday.day
        self.driver_manager.select_option(year_xpath, 0, year_index)
        self.driver_manager.select_option(month_xpath, 0, month_index)
        self.driver_manager.select_option(day_xpath, 0, day_index)

    def set_sex(self):
        sex_xpath = "//input[contains(@type, 'radio') and contains(@name, 'sex')]"
        self.driver_manager.click_element(sex_xpath, self.user_info.sex)

    def set_user_info(self):
        """First, set user info"""
        self.set_lastname()
        self.set_firstname()
        self.set_email()
        self.set_confirm_email()
        self.set_password()
        self.set_birthday()
        self.set_sex()

    def press_register_button(self):
        xpath = "//button[contains(@type, 'submit') and contains(@name, 'websubmit')]"
        self.driver_manager.click_element(xpath, 0)

    def repeat_registration(self):
        self.clear_email()
        self.set_email()
        self.clear_confirm_email()
        self.set_confirm_email()
        self.press_register_button()

    def check_registration(self):
        # error_message_xpath = "//div[@id='reg_error_inner']"
        counter = 0
        while True:
            print(" ... going to check URL")
            current_url = self.driver_manager.get_current_url()
            if EMAIL_CONFIRM_PARTIAL_URL in current_url:
                print(" ... url matched next page")
                break
            else:
                print(" ... wait 2 seconds")
                time.sleep(2)
                counter += 1
                if counter == 5:
                    print(" ... no match in 10 seconds, reset counter and get new email")
                    counter = 0
                    email = self.tm.get_new_email()
                    self.user_info = self.user_info.refresh_email(email)
                    self.repeat_registration()


# _/_/_/_/_/_/_/_/_/_/_/_/_/ -- Page2

    def set_confirmation_code(self, code: str):
        xpath = "//input[contains(@type, 'text') and contains(@id, 'code_in_cliff')]"
        self.driver_manager.set_input(xpath, 0, code)

    def confirm_code(self):
        xpath = "//button[contains(@type, 'submit') and contains(@name, 'confirm')]"
        self.driver_manager.click_element(xpath, 0)

    def close_registed_popup(self):
        """Last, click the OK button of the popup"""
        xpath = "//a[contains(@role, 'button') and contains(text(), 'OK')]"
        self.driver_manager.click_element(xpath, 0)

# _/_/_/_/_/_/_/_/_/_/_/_/_/
# Log out functions
# _/_/_/_/_/_/_/_/_/_/_/_/_/
    def select_menubar_profile_icon(self):
        xpath = "//div[@aria-label='アカウント']/div"
        self.driver_manager.click_element(xpath, 0)

    def select_logout_div(self):
        xpath = "//div[contains(@data-visualcompletion, 'ignore-dynamic') and contains(@data-nocookies, 'true')]/div"
        self.driver_manager.click_element(xpath, 0)

    def logout(self):
        """After registration logout
        Args:
            None
        Returns:
            None
        """

        self.select_menubar_profile_icon()
        self.select_logout_div()

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

def create_account(user_info: UserInfo, tm):
    """Automatically handles registration of a random account with input name.

    Args:
        fullName (str): The name of the new account

    Returns:
        user_info: Return templates with characters in templates.
    """
    print("[facebook] create_account")

    facebook = Facebook(user_info, tm)
    facebook.start()
    facebook.open_top()

    facebook.move_to_register_page()

    # 1/2 page
    facebook.set_user_info()
    facebook.press_register_button()

    facebook.check_registration()

    # # 2/2 page
    # facebook.set_confirmation_code()
    # facebook.confirm_code()

    # facebook.close_registed_popup()
    # facebook.logout()

# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()