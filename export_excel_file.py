"""
This module will export the filtered data received by data_filter.py module into an Excel file.

Author:Steven Sousa
version 1.2
release date - December 2023
"""
import datetime, xlwt, file_name_generator


def export_filtered_results(filtered_list):
    """This function exports the filtered data to an Excel file"""
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Filtered Meteorite Data")
    for column_index, header_name in enumerate(['Name', 'ID', 'Nametype', 'Recclass', 'Mass (g)', 'Fall', 'Year',
                                                'Reclat', 'Reclong', 'Geolocation', 'States', 'Counties']):
        sheet.write(0, column_index, header_name)

    for index, meteorite in enumerate(filtered_list):
        attribute_list = meteorite.to_string().split('\t')
        for attr_index, value in enumerate(attribute_list):
            sheet.write(index + 1, attr_index, value)

    workbook.save(file_name_generator.get_clean_datetime_string() + '.xls')
    exit('\n Program has successfully accomplished its intention and saved your filtered results in a .xls file located'
         ' in the directory where this program resides. Program is now exiting. Goodbye!')
