#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time

from model.chrome import driver_manager

TOP = "https://10minutemail.net/"

class TenMinute(object):

    def __init__(self):
        print("[TenMinute] init")
        self.driver_manager = None

    def start(self):
        if self.driver_manager is None:
            self.driver_manager = driver_manager.DriverManager()
            self.driver_manager.start_driver(True)

    def open_top(self):
        self.driver_manager.open_page(TOP)

    def scrape_email(self):
        xpath = "//input[@class='mailtext']"
        return self.driver_manager.get_input_value(xpath, 0)

    # def reload_page(self):
    #     print(" ... reload")
    #     url = "https://10minutemail.net/new.html"
    #     self.driver_manager.open_page(url)

    def get_mail_count(self):
        xpath = "//table[@id='maillist']/tbody/tr"
        return self.driver_manager.get_elements_count(xpath)

    def get_code(self):
        xpath = "//a[contains(@href, 'readmail.html')]"
        text = self.driver_manager.get_element_text(xpath, 1)
        ## [Twitterの認証コードは******です]
        code = re.sub("\\D", "", text)
        return code

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

    def get_temporary_mail(self):

        self.start()
        self.open_top()

        email = self.scrape_email()
        return email
            
    # def get_new_email(self):
    #     print("new email")
    #     self.reload_page()
    #     email = self.scrape_email()
    #     return email

    def wait_for_code(self):
        while True:
            if self.get_mail_count() == 3:
                print(" ... mail received, break")
                break
            else:
                print(" ... mail not received, wait 10 sec")
                time.sleep(5)
        code = self.get_code()
        return code
        
# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()