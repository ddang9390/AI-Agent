import unittest
from functions.get_files_info import get_files_info, get_file_content

class FileTest(unittest.TestCase):
    # def test_get_files_info(self):
    #     get_files_info("calculator", ".")

    # def test_get_files_info_pkg(self):
    #     get_files_info("calculator", "pkg")

    # def test_get_files_info_bin(self):
    #     get_files_info("calculator", "/bin")

    # def test_get_files_info_prev(self):
    #     get_files_info("calculator", "../")

    def test_get_file_content(self):
        get_file_content("calculator", "lorem.txt")

        get_file_content("calculator", "main.py")
        get_file_content("calculator", "pkg/calculator.py")
        get_file_content("calculator", "/bin/cat")


if __name__ == "__main__":
    unittest.main()