import unittest
from functions.get_files_info import get_files_info

class FileTest(unittest.TestCase):
    def test_get_files_info(self):
        get_files_info("calculator", ".")

    def test_get_files_info_pkg(self):
        get_files_info("calculator", "pkg")

    def test_get_files_info_bin(self):
        get_files_info("calculator", "/bin")

    def test_get_files_info_prev(self):
        get_files_info("calculator", "../")


if __name__ == "__main__":
    unittest.main()