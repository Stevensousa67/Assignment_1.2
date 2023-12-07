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
    filtered_data_sheet = workbook.add_sheet("Filtered Meteorite Data")
    index = 0
    for name in ['Name', 'ID', 'Nametype', 'Recclass', 'Mass (g)', 'Fall', 'Year', 'Reclat', 'Reclong', 'Geolocation', 'States', 'Counties']:
        filtered_data_sheet.write(0, index, name)

    for index in range(len(filtered_list)):
        current_meteorite_object = filtered_list[index]
