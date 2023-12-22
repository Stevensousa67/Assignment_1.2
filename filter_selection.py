"""
This module will ask the user to select which filter mode they'd like to use on the text file they provided.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def get_filename_and_open_mode():
    """This function calls file_opener.py module in order to receive the filename and open mode provided from user input
    in order to send them to data_filter.py later on in this module."""
    import file_opener
    file = file_opener.get_file_name()
    mode = file_opener.get_file_open_mode()
    return file, mode


def select_filter():
    """This function will prompt the user to choose a filter to be used on the file provided in file_opener.py module
    or to quit the program."""
    while True:
        choice = input('\nPlease select one of the options below:\n'
                       '1. Filter by MASS(g)\n'
                       '2. Filter by YEAR\n'
                       '3. EXIT the program\n')

        if check_if_filter_choice_is_valid(choice):
            return choice
        else:
            print('\nPlease select a valid option.')


def check_if_filter_choice_is_valid(choice):
    """This function will check to see if the option selected by the user in select_filter() is valid."""
    if choice in ['1', '2']:
        return True
    elif choice == '3':
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def select_mass():
    """This function requests a lower and upper bound limits from the user if they chose to filter the data by mass. If
    a user enters a lower limit that is greater than the upper limit, they will be swapped. Also, if the user enters
    a negative lower bound, it will be set to 0."""
    mass_lower_limit = get_valid_int_input("\nEnter the LOWER limit (inclusive) for the meteor's mass (g)."
                                           " (To EXIT, type 'Q'): \n")

    mass_upper_limit = get_valid_int_input("\nEnter the UPPER limit (inclusive) for the meteor's mass (g). "
                                           "(To EXIT, type 'Q'): \n")

    if mass_lower_limit > mass_upper_limit:
        mass_lower_limit, mass_upper_limit = swap_values_between_bounds(mass_lower_limit, mass_upper_limit)
        print('\nBecause you entered a lower bound that is higher than the upper bound, the program has readjusted the'
              'bounds so that the lower bound can be the smallest value you inputted.')

    if mass_lower_limit <= 0:
        mass_lower_limit = 1

    print('\nSelected mass range (g): ', mass_lower_limit, ' - ', mass_upper_limit)
    return mass_lower_limit, mass_upper_limit


def select_year():
    """This function requests a lower and upper bound limits from user if they chose to filter the data on year. If
    a user enters a lower limit that is greater than the upper limit, they will be swapped. Also, if the user enters
    a negative lower bound, it will be set to 0."""
    year_lower_limit = get_valid_int_input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the "
                                           "meteorite fell on Earth. \nThis allows the table to display meteors from "
                                           "that year onward only. (To EXIT, type 'Q'): \n")

    year_upper_limit = get_valid_int_input("\nIn YYYY format, enter the UPPER limit (inclusive) for the year the "
                                           "meteorite fell on Earth. \nThis allows the table to display meteors from "
                                           "that year onward only. (To EXIT, type 'Q'): \n")

    if year_lower_limit > year_upper_limit:
        year_lower_limit, year_upper_limit = swap_values_between_bounds(year_lower_limit, year_upper_limit)

    if year_lower_limit < 0:
        year_lower_limit = 0

    print('\nSelected year range: ', year_lower_limit, ' - ', year_upper_limit)
    return year_lower_limit, year_upper_limit


def get_valid_int_input(prompt):
    """This function checks if the user input for select_mass() or select_year() are valid, or quits the program if the
    user typed '>q' or ':q' during either the lower limit or upper limit requests of both functions."""
    while True:
        user_input = input(prompt)
        if user_input == 'Q':
            exit('\nProgram is now exiting. Goodbye!')
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("\nInvalid range limit: ", user_input)


def swap_values_between_bounds(lower_limit, upper_limit):
    """This function handles the situation where the user typed a lower bound limit that is larger than the upper bound
    limit, making the lower limit the smaller value inputted and the upper limit the larger value."""
    int(lower_limit), int(upper_limit)
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit
    print('\nBecause you entered a lower bound that is higher than the upper bound, the program has readjusted the'
          'bounds so that the lower bound can be the smallest value you inputted.')
    return lower_limit, upper_limit
