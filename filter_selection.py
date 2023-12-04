def select_filter():
    """This function will prompt the user to choose a filter to be used on the file provided in file_opener.py module
    or to quit the program."""
    while True:
        choice = input('\nPlease select one of the options below:\n'
                       '\'1\' - Filter by MASS(g)\n'
                       '\'2\' - Filter by YEAR\n'
                       '\'3\' - EXIT the program\n')

        if check_if_filter_choice_is_valid(choice):
            if choice == '1':
                select_mass()
                break
            elif choice == '2':
                select_year()
                break
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
    """This function requests a lower and upper bound limits from the user if they chose to filter the data by mass."""
    while True:
        mass_lower_limit = input("\nEnter the LOWER limit (inclusive) for the meteor's mass (g)."
                                 " (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

        if check_if_user_input_is_valid_int(mass_lower_limit):
            break
        else:
            print("\nPlease type a valid lower bound for mass(g).")

    while True:
        mass_upper_limit = input("\nEnter the UPPER limit (inclusive) for the meteor's mass (g). "
                                 "(To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

        if check_if_user_input_is_valid_int(mass_upper_limit):
            break
        else:
            print("\nPlease type a valid upper bound for mass(g).")

    if mass_lower_limit > mass_upper_limit:
        mass_lower_limit, mass_upper_limit = swap_values_for_bounds(mass_lower_limit, mass_upper_limit)
        print('\nBecause you entered a lower bound that is higher than the upper bound, the program has readjusted the'
              'bounds so that the lower bound can be the smallest value you inputted.')

    print('\nSelected mass range (g): ', mass_lower_limit, ' - ', mass_upper_limit)
    # data_filter.filter_mass(file_name, read_mode, int(mass_lower_limit), int(mass_upper_limit))


def select_year():
    """This function requests a lower and upper bound limits from user if they chose to filter the data on year."""
    while True:
        year_lower_limit = input('\nIn YYYY format, enter the UPPER limit (inclusive) for the year the meteorite fell '
                                 'on Earth. \nThis allows the table to display meteors from that year onward only. '
                                 '(To EXIT in Windows, type \'>q\' or \'>Q\'. In macOS, type \':Q\' or \':q\'): \n')

        if check_if_user_input_is_valid_int(year_lower_limit):
            break
        else:
            print("\nPlease type a valid lower bound year in the format YYYY.")

    while True:
        year_upper_limit = input('\nIn YYYY format, enter the UPPER limit (inclusive) for the year the meteorite fell '
                                 'on Earth. \nThis allows the table to display meteors from that year onward only. '
                                 '(To EXIT in Windows, type \'>q\' or \'>Q\'. In macOS, type \':Q\' or \':q\'): \n')

        if check_if_user_input_is_valid_int(year_upper_limit):
            break
        else:
            print("\nPlease type a valid upper bound year in the format YYYY.")

    if year_lower_limit > year_upper_limit:
        year_lower_limit, year_upper_limit = swap_values_for_bounds(int(year_lower_limit), int(year_upper_limit))
        print('\nBecause you entered a lower bound that is higher than the upper bound, the program has readjusted the'
              'bounds so that the lower bound can be the smallest value you inputted.')

    print('\nSelected year range: ', year_lower_limit, ' - ', year_upper_limit)
    # data_filter.filter_year(file_name, read_mode, year_lower_limit, year_upper_limit)


def check_if_user_input_is_valid_int(user_input):
    """This function checks if the user input for select_mass() or select_year() are valid, or quits the program if the
    user typed '>q' or ':q' during either the lower limit or upper limit requests of both functions."""
    if user_input.lower() in [">q", ":q"]:
        exit('\nProgram is now exiting. Goodbye!')
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def make_user_input_equal_1(user_input):
    """This function handles inputs that are <= 0 during select_mass() and select_year() execution, converting them to 1
    because those values don't exist for mass and year."""
    user_input = 1
    return user_input


def swap_values_for_bounds(lower_limit, upper_limit):
    """This function handles the situation where the user typed a lower bound limit that is larger than the upper bound
    limit, making the lower limit the smaller value inputted and the upper limit the larger value."""
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit
    return lower_limit, upper_limit
