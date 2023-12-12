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
          'Welcome to the meteor filtering program! This program will open a .txt file containing data entries of '
          'meteorites recorded by NASA to filter.\nIt will then ask you if you would like to filter the data by '
          'choosing either the mass of the meteorite or the year it fell on Earth.\nAfter filtering, the program will '
          'ask if you would like the data to be displayed in the terminal, exported to a .txt file, or to a .xls file. '
          '\nAfter displaying or exporting, the program will exit.')
