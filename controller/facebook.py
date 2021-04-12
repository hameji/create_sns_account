#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random

from model.chrome import driver_manager

TOP = "https://www.facebook.com/"

class Facebook(object):

    def __init__(self):
        print("[Facebook] init")
        self.driver_manager = None
        self.user_info = None

    def start(self):
        if self.driver_manager is None:
            print("start")
            self.driver_manager.DriverManager()
            self.driver_manager.start_driver()

    def open_top(self):
        self.driver_manager.open_page(TOP)

    def __del__(self):
        self.driver_manager.__del__()

# _/_/_/_/_/_/_/_/_/_/_/_/_/
# Register functions
# _/_/_/_/_/_/_/_/_/_/_/_/_/

    def move_to_register_page(self): 
        """Move from top page to register page"""
        xpath = "//a[contains(@role, 'button') and contains(text(), '新しいアカウントを作成')]" 
        self.driver_manager.click_element(xpath, 0)

    def set_lastname(self, lastname: str):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'lastname')]"
        self.driver_manager.set_input(xpath, 0, lastname)

    def set_firstname(self, firstname: str):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'firstname')]"
        self.driver_manager.set_input(xpath, 0, firstname)

    def set_email(self, email: str):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'reg_email__')]"
        self.driver_manager.set_input(xpath, 0, email)

    def set_confirm_email(self, email: str):
        xpath = "//input[contains(@type, 'text') and contains(@name, 'reg_email_confirmation__')]"
        self.driver_manager.set_input(xpath, 0, email)

    def set_password(self, password: str):
        xpath = "//input[contains(@type, 'password') and contains(@name, 'reg_passwd__')]"
        self.driver_manager.set_input(xpath, 0, password)

    def set_birthday(self):
        year_xpath = "//select[@id='year']"
        month_xpath = "//select[@id='month']"
        day_xpath = "//select[@id='day']"
        self.driver_manager.select_option(year_xpath, 0, 18, 65)
        self.driver_manager.select_option(month_xpath, 0, 0, 11)
        self.driver_manager.select_option(day_xpath, 0, 0, 28)

    def set_sex(self):
        sex_xpath = "//input[contains(@type, 'radio') and contains(@name, 'sex')]"
        sex_index = random.randint(1,2)
        self.driver_manager.click_element(sex_xpath, sex_index)

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

    def repeat_registration(self, user_info):
        self.set_email()
        self.press_register_button()

    def check_registration(self):
        next_url = "https://www.facebook.com/confirmemail.php?next="
        # error_message_xpath = "//div[@id='reg_error_inner']"
        counter = 0
        while True:
            current_url = self.driver_manager.get_current_url()
            if next_url in current_url:
                break
            else:
                time.sleep(2)
                counter += 1
                if counter == 5:
                    self.user_info = UserInfo.refresh_email(self.user_info)
                    self.repeat_registration()

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

def create_account(fullName: str):
    """Automatically handles registration of a random account with input name.

    Args:
        fullName (str): The name of the new account

    Returns:
        string.Template: Return templates with characters in templates.
    """
    print("create_account")

    facebook = Facebook()
    facebook.start()
    facebook.open_top()

    facebook.move_to_register_page()

    # 1/2 page
    facebook.set_user_info()
    facebook.press_register_button()

    # 2/2 page
    facebook.set_confirmation_code()
    facebook.confirm_code()

    facebook.close_registed_popup()
    facebook.logout()

# main処理
def main():
    print("main")


# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
