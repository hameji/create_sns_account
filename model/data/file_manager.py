#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import csv
import os
import pathlib

ACCOUNT_COLUMN_NAME = 'NAME'
ACCOUNT_COLUMN_EMAIL = 'EMAIL'
ACCOUNT_COLUMN_PASSWORD = 'PASSWORD'
ACCOUNT_CSV_FILE_PATH = 'user_accounts.csv'

class CsvModel(object):
    """Base csv model."""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()

class AccountModel(CsvModel):
    """Definition of class that generates account model to write to CSV"""
    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
        super().__init__(csv_file, *args, **kwargs)
        self.column = [ACCOUNT_COLUMN_NAME, ACCOUNT_COLUMN_EMAIL, ACCOUNT_COLUMN_PASSWORD]

    def get_csv_file_path(self):
        """Set csv file path.

        Use csv path if set in settings, otherwise use default
        """
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = ACCOUNT_CSV_FILE_PATH
        return csv_file_path

    def save(self, user_info_data):
        """Save data to csv file."""
        with open(self.csv_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(user_info_data)
            
# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()