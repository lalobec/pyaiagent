# tests.py in root

import unittest
from functions.get_files_info import get_files_info


class TestGetFilesFunc(unittest.TestCase):
    def test_one(self):
        print(get_files_info("calculator", "."))

    def test_two(self):
        print(get_files_info("calculator", "pkg"))

    def test_three(self):
        print(get_files_info("calculator", "/bin"))

    def test_four(self):
        print(get_files_info("calculator", "../"))


if __name__ == "__main__":
    unittest.main()
