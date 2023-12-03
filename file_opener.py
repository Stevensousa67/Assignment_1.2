"""
This module will open the meteorite_landings_data.txt file and ask the user to select which read mode they'd like.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def get_file_name():
    while True:
        filename = input('\nEnter a file name with its extension (ex: "file_name.txt") or\n'
                         'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ').lower()

        if filename_is_valid(filename):
            print("\nTarget file: ", filename)
            return filename
        else:
            print("Invalid filename. Please type a valid file name.")


def filename_is_valid(filename):
    if filename.endswith(".txt"):
        return True
    elif filename in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    else:
        return False


def get_file_open_mode():
    open_mode = input('\nFrom the list below, what mode would you like to open this file with?\n'
                      '"r" - open for reading (default)\n'
                      '"w" - open for writing, truncating the file first\n'
                      '"x" - open for exclusive creation, failing if the file already exists\n'
                      '"a" - open for writing, appending to the end of file if it exists\n'
                      'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ').lower()

    print('\nSelected open mode: ', open_mode)

    if open_mode in ['>q', ':q']: exit('\nProgram is now exiting. Goodbye!')
    return open_mode


file_name = get_file_name()
open_mode = get_file_open_mode()
