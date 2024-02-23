import pytest
import os
from app.utils.find_json_file import find_json_file


def test_find_json_file_exists(tmp_path):
    directory = tmp_path / "data"
    directory.mkdir()
    temp_file = directory / "test_file.json"
    temp_file.write_text('{"test": true}')

    assert find_json_file(str(directory)) == str(temp_file)


def test_find_json_file_not_found(tmp_path):
    directory = tmp_path / "empty_data"
    directory.mkdir()

    with pytest.raises(FileNotFoundError):
        find_json_file(str(directory))
