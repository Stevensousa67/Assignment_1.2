def select_filter():
    while True:
        choice = input('\nPlease select one of the options below:\n'
                       '\'1\' - Filter by MASS(g)\n'
                       '\'2\' - Filter by YEAR\n'
                       '\'3\' - EXIT the program\n')

        if check_if_filter_choice_is_valid(choice):
            if choice == '1':
                select_mass()
            elif choice == '2':
                select_year()
        else:
            print('\nPlease select a valid option.')


def check_if_filter_choice_is_valid(choice):
    if choice in ['1', '2']:
        return True
    elif choice == '3':
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def select_mass():
    mass_lower_limit = input("\nEnter the LOWER limit (inclusive) for the meteor's mass (g) without commas or decimal "
                             "points. (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if mass_lower_limit.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')

    mass_upper_limit = input("Enter the UPPER limit (inclusive) for the meteor's mass (g) without commas or decimal "
                             "points. (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if mass_upper_limit.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')

    print('\nSelected mass range (g): ', mass_lower_limit, ' - ', mass_upper_limit)

    # data_filter.filter_mass(file_name, read_mode, int(mass_lower_limit), int(mass_upper_limit))


def select_year():
    year_lower_limit = input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the meteorite fell on "
                             "Earth. \nThis allows the table to display meteors from that year onward only. (To EXIT "
                             "in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if year_lower_limit.lower() in [">q", ":q"]:
        exit('\nProgram is now exiting. Goodbye!')

    year_upper_limit = input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the meteorite fell on "
                             "Earth. \nThis allows the table to display meteors from that year onward only. (To EXIT "
                             "in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if year_upper_limit.lower() in [">q", ":q"]:
        exit('\nProgram is now exiting. Goodbye!')

    # data_filter.filter_year(file_name, read_mode, int(year_lower_limit), int(year_upper_limit))

# def check_if_year_is_valid(year):
