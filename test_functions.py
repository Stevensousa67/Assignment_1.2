import pytest

import file_opener


def test_check_if_file_name_is_valid():
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
