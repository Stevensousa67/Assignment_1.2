"""
This module will generate the file name for the exported data file.

Author:Steven Sousa
version 1.2
release date - December 2023
"""

import datetime


def get_clean_datetime_string():
    """This function generates the file name for the exported data for both .txt and .xls"""
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str
