"""
This module will greet the user and explain how the program will operate.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def print_welcome_message():
    """This function will greet the user when the program initiates and explain what the program does and what is
     expected from the user."""
    print('\nAuthor: Steven Sousa / Version: 1.2 / Release Date: December 2023\n\n'
          'Welcome to the meteor filtering program! This program opens a .txt file from NASA to filter the data by '
          'choosing either the mass of the meteorite or the year it fell on Earth.\nAfter filtering, the program will'
          ' ask if you would like the data to be displayed in the Terminal, exported to a .txt file, '
          'or to an .xlsm file.')


def run_filter_selection():
    """This function will initiate the filter_selection.py module"""
    import filter_selection
    filter_selection


print_welcome_message()
run_filter_selection()