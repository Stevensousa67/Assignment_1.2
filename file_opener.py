"""
This module will open the meteorite_landings_data.txt file and ask the user to select which read mode they'd like.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""

def get_file_name():
    while True:
        filename = input('\nEnter a file name with its extension (ex: "file_name.txt") or\n'
                         'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

        if check_if_filename_is_valid(filename):
            print("\nTarget file: ", filename)
            return filename
        else:
            print("Invalid filename. Please type a valid file name.")


def check_if_filename_is_valid(filename):
    if filename.lower().endswith(".txt"):
        return True
    elif filename.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def get_file_open_mode():
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
    if mode.lower() in ['r', 'w', 'x', 'a']:
        return True
    elif mode.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def run_filter_selection():
    import filter_selection
    filter_selection.select_filter()


file_name = get_file_name()
open_mode = get_file_open_mode()
run_filter_selection()
