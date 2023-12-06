"""
This module will export the filtered data received by data_filter.py module into a text file.

Author:Steven Sousa
version 1.2
release date - December 2023
"""
import datetime


def export_filtered_results(filtered_list):
    """This function exports the filtered data to a text file."""
    header = 'name\tid\tnametype\trecclass\tmass (g)\tfall\tyear\treclat\treclong\tgeolocation\tstates\tcounties'
    output_file_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file_name += '.txt'
    output_file = open(output_file_name, 'w+')
    output_file.write(header + '\n')
    for meteorite in filtered_list:
        output_file.write(meteorite.to_string() + '\n')
    output_file.close()
    exit('\nProgram has successfully accomplished its intention and saved your filtered results in a text file located'
         ' in the directory where this program resides. Program is now exiting. Goodbye!')
