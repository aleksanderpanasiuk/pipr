from file import FileInfo
import pytest


def test_file_init():
    file = FileInfo("sad.txt")

    assert file.path == "sad.txt"
    assert file.name == "sad.txt"
    assert file.number_of_lines == 3


def test_file_init_file_not_found():
    with pytest.raises(FileNotFoundError):
        file = FileInfo("sss.txt")

        assert file.path == "sad.txt"
        assert file.name == "sad.txt"
        assert file.number_of_lines == 3


def test_file_new_file():
    file = FileInfo("sad.txt")

    assert file.path == "sad.txt"
    assert file.name == "sad.txt"
    assert file.number_of_lines == 3

    file.new_file("das.txt")
    assert file.path == "das.txt"
    assert file.name == "das.txt"
    assert file.number_of_lines == 5
