"""
This module will open the meteorite_landings_data.txt file and ask the user to select which read mode they'd like.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


def get_file_name():
    file_name = input('Enter a valid file name (ex. "file_name.txt") with its file extension (if applicable) or\n'
                      'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

    print("\nTarget file: ", file_name)

    if file_name.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    return file_name


def get_file_open_mode():
    open_mode = input('\nFrom the list below, what mode would you like to open this file with?\n'
                      '"r" - open for reading (default)\n'
                      '"w" - open for writing, truncating the file first\n'
                      '"x" - open for exclusive creation, failing if the file already exists\n'
                      '"a" - open for writing, appending to the end of file if it exists\n'
                      'To EXIT in Windows, type ">q" or ">Q". In macOS, type ":Q" or ":q": ')

    print('\nSelected read mode: ', open_mode)

    if open_mode.lower() in ['>q', ':q']:
        exit('\nProgram is now exiting. Goodbye!')
    return open_mode


file_name = get_file_name()
open_mode = get_file_open_mode()
