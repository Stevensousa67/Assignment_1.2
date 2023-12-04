"""
This module will open the meteorite_landings_data.txt file and ask the user to select which read mode they'd like.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def get_file_name():
    """This function will prompt the user to provide a text file for the program to filter on."""
    while True:
        filename = input('\nEnter a file name with its extension (ex: "file_name.txt") or\n'
                         'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

        if check_if_filename_is_valid(filename):
            print("\nTarget file: ", filename)
            break
        else:
            print("Invalid filename. Please type a valid file name.")
    return filename


def check_if_filename_is_valid(filename):
    """This function will check if the filename provided by the user is valid (ending in .txt) or if the user decided
    to quit the program by typing '>q' or ':q' during filename request."""
    if filename.lower().endswith(".txt"):
        return True
    elif filename.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def get_file_open_mode():
    """This function will prompt the user to choose an open mode for the file that was provided to the program."""
    while True:
        mode = input('\nFrom the list below, what mode would you like to open this file with?\n'
                     '"r" - open for reading (default)\n'
                     '"w" - open for writing, truncating the file first. **WARNING**: This will delete the '
                     'contents of an existing file! \n'
                     '"x" - open for exclusive creation, failing if the file already exists\n'
                     '"a" - open for writing, appending to the end of file if it exists\n'
                     'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

        if check_if_open_mode_is_valid(mode):
            print('\nSelected open mode: ', mode)
            return mode
        else:
            print("Invalid mode. Please type a valid mode.")


def check_if_open_mode_is_valid(mode):
    """This function check to see if the file mode provided by the user is valid or quit the program if the user typed
    '>q' or ':q' during open mode request."""
    if mode.lower() in ['r', 'w', 'x', 'a']:
        return True
    elif mode.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def run_filter_selection():
    """This function will call the run_filter_selection.py module once filename and open mode have been provided and
    verified as valid inputs."""
    import filter_selection
    filter_selection.select_filter()


file_name = get_file_name()
open_mode = get_file_open_mode()
run_filter_selection()
