"""
The purpose of this application is to filter a large data set from NASA. The target dataset is a collection of 45,716
data entries. Each entry has information about a single meteorite landing on Earth. During runtime, the user
will select if the data should be filtered by mass - and consequently set the upper and lower bounds of the mass filter
 - or by year the meteorite fell onto Earth. Finally, the user will be asked if they'd like the data to be displayed in
 the Terminal, exported to a .txt file or .xlsm file.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""
import data_filter
import export_excel_file
import export_txt_file
import filter_selection
import show_results_selection
import terminal_table
import welcome_message


def call_correct_display_method(file_name, open_mode, filter_function, *args):
    """This function asks the user which way to display the filtered data"""
    filter_result = filter_function(file_name, open_mode, *args)
    display_results_choice = show_results_selection.select_results_display()
    if display_results_choice == '1':
        terminal_table.print_filtered_list(filter_result)
    elif display_results_choice == '2':
        export_txt_file.export_filtered_results(filter_result)
    elif display_results_choice == '3':
        export_excel_file.export_filtered_results(filter_result)


def main():
    """This function is the main program. Execute it to start the filtering program."""
    welcome_message.print_welcome_message()
    file_name, open_mode = filter_selection.get_filename_and_open_mode()
    filter_choice = filter_selection.select_filter()

    if filter_choice == '1':
        mass_lower_bound, mass_upper_bound = filter_selection.select_mass()
        call_correct_display_method(file_name, open_mode, data_filter.filter_mass, mass_lower_bound, mass_upper_bound)

    elif filter_choice == '2':
        year_lower_bound, year_upper_bound = filter_selection.select_year()
        call_correct_display_method(file_name, open_mode, data_filter.filter_year, year_lower_bound, year_upper_bound)


if __name__ == '__main__':
    main()
