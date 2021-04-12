#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.chrome import driver_manager

TOP = "https://www.facebook.com/"

class Facebook(object):

    def __init__(self):
        print("start")
        self.driver_manager = driver_manager.DriverManager()

    def start(self):
        self.driver_manager.start_driver()

    def open_top(self):
        self.driver_manager.open_page(TOP)

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

def create_account(fullName: str):
    print("create_account")

    facebook = Facebook()
    facebook.start()
    facebook.open_top()


# main処理
def main():
    print("main")


# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()

