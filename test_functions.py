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
    assert file_opener.check_if_filename_is_valid('data.txt') == True
    assert file_opener.check_if_filename_is_valid('data') == False
    assert file_opener.check_if_filename_is_valid('.txt') == False
    assert file_opener.check_if_filename_is_valid('') == False
    with pytest.raises(SystemExit): file_opener.check_if_filename_is_valid(':q')
    with pytest.raises(SystemExit): file_opener.check_if_filename_is_valid(':Q')
    with pytest.raises(SystemExit): file_opener.check_if_filename_is_valid('>q')
    with pytest.raises(SystemExit): file_opener.check_if_filename_is_valid('>Q')
    with pytest.raises(TypeError): file_opener.check_if_filename_is_valid(None)
    with pytest.raises(TypeError): file_opener.check_if_filename_is_valid()
    with pytest.raises(AttributeError): file_opener.check_if_filename_is_valid(123)
    with pytest.raises(AttributeError): file_opener.check_if_filename_is_valid(False)
    with pytest.raises(AttributeError): file_opener.check_if_filename_is_valid(True)
