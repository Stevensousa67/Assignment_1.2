"""
This module will greet the user and explain how the program will operate.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def print_welcome_message():
      print('\nAuthor: Steven Sousa / Version: 1.2 / Release Date: December 2023\n\n'
            'Welcome to the meteor filtering program! This program opens a .txt file from NASA to filter the data by '
            'choosing either the mass of the meteorite or the year it fell on Earth.\nAfter filtering, the program will'
            ' ask if you would like the data to be displayed in the Terminal, exported to a .txt file, '
            'or to an .xlsm file.')


def run_file_opener():
      import file_opener
      file_opener.get_file_name()


print_welcome_message()
run_file_opener()
