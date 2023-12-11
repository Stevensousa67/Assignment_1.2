"""
This module provides 3 tests for functions contained within the Assignment 1.2 project.

Author: Steven Sousa
version: 1.2
release date: December 2023
"""


import pytest

import file_opener


def test_check_if_filename_is_valid():
    """This function tests the check_if_filename_is_valid function from file_opener.py"""
    valid_inputs = ['Data.txt', 'meteorite_landings_data.txt']
    invalid_inputs = ['data, meteorite_landings_data', '.txt', '', '123', 'gesfd']
    exit_inputs = [':q', ':Q', '>q', '>Q']
    error_inputs = [(), None, 123, False, True, 3.4]

    # The following block of tests ensures that the expected inputs from valid_inputs are True during runtime
    for file_name in valid_inputs:
        assert file_opener.check_if_filename_is_valid(file_name)

    # The following block of tests ensures that inputs from invalid_inputs are False during runtime
    for file_name in invalid_inputs:
        assert not file_opener.check_if_filename_is_valid(file_name)

    # The following block of tests ensures that typing any exit inout will exit the program
    for exit_choice in exit_inputs:
        with pytest.raises(SystemExit): file_opener.check_if_filename_is_valid(exit_choice)

    # The following block of tests ensures that if the inputs from error_inputs are entered, errors are raised
    for mode in error_inputs:
        with pytest.raises((TypeError, AttributeError)): file_opener.check_if_filename_is_valid(mode)


def test_check_if_open_mode_is_valid():
    """This functions tests the check_if_open_mode_is_valid function from file_opener.py"""
    valid_modes = {'r', 'w', 'x', 'a'}
    all_characters = [chr(i) for i in range(128)]  # ASCII characters
    invalid_modes = [char.lower() for char in all_characters if char.lower() not in valid_modes]
    exit_inputs = [':q', ':Q', '>q', '>Q']
    error_inputs = [(), None, 123, False, True, 3.4]

    # The following block of tests ensures that the expected inputs from valid_modes are True during runtime
    for mode in valid_modes:
        assert file_opener.check_if_open_mode_is_valid(mode)

    # The following block of tests ensures that inputs from invalid_modes are False during runtime
    for mode in invalid_modes:
        assert not file_opener.check_if_open_mode_is_valid(mode)

    # The following block of tests ensures that typing any exit inout will exit the program
    for exit_choice in exit_inputs:
        with pytest.raises(SystemExit): file_opener.check_if_open_mode_is_valid(exit_choice)

    # The following block of tests ensures that if the inputs from error_inputs are entered, errors are raised
    for mode in error_inputs:
        with pytest.raises((TypeError, AttributeError)): file_opener.check_if_open_mode_is_valid(mode)

