def get_user_choice():
    try:
        return int(input('\nEnter your choice (or "3" to quit): '))
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return None


def select_filter(file_name):
    options = {1: select_mass, 2: select_year}
    print('\n'.join([f'"{key}" - {label}' for key, (label, _) in options.items()]))
    choice = int(input('\nEnter your choice (or "3" to quit): ') or 0)

    print("\nFilter selected: ", choice)

    if choice == 3: exit('\nProgram is now exiting. Goodbye!')

    selected_function = options.get(choice)
    (selected_function or (lambda: print('Invalid choice. Please select 1, 2, or 3.')))()


def select_mass():
    mass_lower_limit = input("\nEnter the LOWER limit (inclusive) for the meteor's mass (g) without commas or decimal "
                             "points. (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if mass_lower_limit.lower() in ['>q', ':q']:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    mass_upper_limit = input("Enter the UPPER limit (inclusive) for the meteor's mass (g) without commas or decimal "
                             "points. (To EXIT in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if mass_upper_limit.lower() in ['>q', ':q']:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    print('\nSelected mass range (g): ', mass_lower_limit, ' - ', mass_upper_limit)

    # data_filter.filter_mass(file_name, read_mode, int(mass_lower_limit), int(mass_upper_limit))


def select_year():
    year_lower_limit = input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the meteorite fell on "
                             "Earth. \nThis allows the table to display meteors from that year onward only. (To EXIT "
                             "in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if year_lower_limit.lower() in [">q", ":q"]:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    year_upper_limit = input("\nIn YYYY format, enter the LOWER limit (inclusive) for the year the meteorite fell on "
                             "Earth. \nThis allows the table to display meteors from that year onward only. (To EXIT "
                             "in Windows, type '>q' or '>Q'. In macOS, type ':Q' or ':q'): \n")

    if year_upper_limit.lower() in [">q", ":q"]:
        print('\nProgram is now exiting. Goodbye!')
        exit()

    # data_filter.filter_year(file_name, read_mode, int(year_lower_limit), int(year_upper_limit))
