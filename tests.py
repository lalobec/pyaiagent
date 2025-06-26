# tests.py in root

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


class TestGetFilesFunc(unittest.TestCase):
    """
    def test_one(self):
        print(get_files_info("calculator", "."))

    def test_two(self):
        print(get_files_info("calculator", "pkg"))

    def test_three(self):
        print(get_files_info("calculator", "/bin"))

    def test_four(self):
        print(get_files_info("calculator", "../"))

    def test_file_content(self):
        print(get_file_content("calculator", "lorem.txt"))

    def test_file_content_1(self):
        print(get_file_content("calculator", "main.py"))

    def test_file_content_2(self):
        print(get_file_content("calculator", "pkg/calculator.py"))

    def test_file_content_3(self):
        print(get_file_content("calculator", "/bin/cat"))

    def test_write_file1(self):
        print(write_file("calculator", "lorem.txt", "wait,
        this isn't lorem ipsum"))

    def test_write_file2(self):
        print(write_file("calculator", "pkg/morelorem.txt",
        "lorem ipsum dolor sit amet"))

    def test_write_file3(self):
        print(write_file("calculator", "/tmp/temp.txt",
        "this should not be allowed"))
    """

    def test_run_python_file1(self):
        print(run_python_file("calculator", "main.py"))

    def test_run_python_file2(self):
        print(run_python_file("calculator", "tests.py"))

    def test_run_python_file3(self):
        print(run_python_file("calculator", "../main.py"))

    def test_run_python_file4(self):
        print(run_python_file("calculator", "nonexistent.py"))


if __name__ == "__main__":
    unittest.main()
