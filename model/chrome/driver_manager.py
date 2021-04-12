#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import random

from selenium import webdriver
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException

from model.error import chrome_error

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_

class DriverManager(object):

    def __init__(self):
        self.driver = None
        # self.WAIT = WebDriverWait(self.driver, 30)

    def set_options(self):
        """Set chrome driver option"""
        options = webdriver.ChromeOptions()
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        # options.add_argument('--disable-web-security')
        # options.add_argument('--allow-running^insecure-content')
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_extension('XXXXXXX.crx')
        # options.add_argument('--user-data-dir=profile')
        options.add_argument('--incognito') # シークレットモードの設定を付与
        # options.add_argument(f'--proxy-server={settings.TOR_PROXY}') # Torのプロキシを使用
        # options.add_argument('--proxy-server=http://153.122.60.209:8080') # Free Proxy
        # options.add_argument('--headless') # ヘッドレスモード（画面非表示モード)の設定
        options.add_experimental_option("detach", True)
        return options

    def start_driver(self):
        """If driver is none set driver"""
        if self.driver is None:
            driver_options = self.set_options()
            if os.name == 'nt': #Windows
                DRIVER_NAME = "chromedriver.exe"
            elif os.name == 'posix': #Mac
                DRIVER_NAME = "chromedriver"
            self.driver = webdriver.Chrome(executable_path=os.getcwd() + "/model/chrome/" + DRIVER_NAME, options=driver_options)

    def open_page(self, url: str):
        """Open url with chrome driver"""
        print(f" ... going to open page [{url}]")
        self.driver.get(url)
        time.sleep(3)
        # WebDriverWait(driver, timeout=3).until(document_initialised)

    def switch_frames(self, xpath: str):
        """Switch frames for iFrame tag"""
        iFrame = self.driver.find_elements_by_xpath(xpath)
        self.driver.switch_to.frame(iFrame)

    def get_elements(self, xpath: str):
        """Get html element and return"""
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements
        
    def get_element_text(self, xpath: str, index: int):
        """Get html element's text"""
        elements = self.driver.find_elements_by_xpath(xpath)
        print(f" ... found {len(elements)} element for text")
        if index > len(elements) - 1:
            raise chrome_error.ChromeElementCountError
        return elements[index].text

    def set_input(self, xpath: str, index: int, input: str):
        """Set html input text"""
        time.sleep(0.5)
        input_elements = self.driver.find_elements_by_xpath(xpath)
        print(f" ... found {len(input_elements)} inputs")
        if index > len(input_elements) - 1:
            raise chrome_error.ChromeElementCountError
        input_elements[index].send_keys(input)

    def select_option(self, xpath: str, option_index: int, start_index: int, end_index: int):
        """Set index of html option tag"""
        option_elements = self.driver.find_elements_by_xpath(xpath)
        if option_index > len(option_elements) - 1:
            raise chrome_error.ChromeElementCountError
        select = Select(option_elements[option_index])
        index = random.randint(start_index, end_index)
        select.select_by_index(index)
        time.sleep(0.5)

    def click_element(self, xpath: str, index: int):
        """Click element"""
        # element = WAIT.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # element.click()
        time.sleep(2)
        elements = self.driver.find_elements_by_xpath(xpath)
        print(f" ... found {len(elements)} element for click")
        if index > len(elements) - 1:
            raise chrome_error.ChromeElementCountError
        elements[index].click()
        time.sleep(5)

    def close_driver(self):
        """Close chrome driver"""
        if self.driver is not None:
            self.driver.close()

    def quit_driver(self):
        """Quit chrome driver"""
        if self.driver is not None:
            self.driver.quit()

    def __del__(self):
        """Destructor"""
        self.close_driver()
        self.quit_driver()

# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()