"""
This module will export the filtered data received by data_filter.py module into an Excel file.

Author:Steven Sousa
version 1.2
release date - December 2023
"""
import datetime

import xlwt


def export_filtered_results(filtered_list):
    """This function exports the filtered data to an Excel file"""
    workbook_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("Filtered Data")
    row_num = 0
    columns = ['ID', 'Title', 'Description']