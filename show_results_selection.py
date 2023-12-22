"""
This module will ask the user to select which method they'd like to use to display their filtered data results.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def select_results_display():
    """This function will prompt the user to choose a method on how to display the filtered data. The user can choose
    between terminal display, .txt file, .csv file, or to quit the program."""
    while True:
        choice = input('\nPlease select one of the options below to display the filtered results:\n'
                       '1. Terminal\n'
                       '2. Save to text file (.txt)\n'
                       '3. Save to Excel file (.csv)\n'
                       '4. EXIT the program\n')

        if check_if_filter_choice_is_valid(choice):
            return choice
        else:
            print('\nPlease select a valid option.')


def check_if_filter_choice_is_valid(choice):
    """This function will check to see if the option selected by the user in select_filter() is valid."""
    if choice in ['1', '2', '3']:
        return True
    elif choice == '4':
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False
