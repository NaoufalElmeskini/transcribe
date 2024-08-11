import unittest

from transcribe import extract_file_name


class TestExtractFileName(unittest.TestCase):

    def test_extract_file_name(self):
        url = "https://www.youtube.com/watch?v=3JZ_D3ELwOQ"
        result = extract_file_name(url)
        self.assertEqual(result, "watch?v=3JZ_D3ELwOQ")

    def test_extract_file_name_with_no_slash(self):
        url = "https://www.youtube.com"
        result = extract_file_name(url)
        self.assertEqual(result, "")

    def test_extract_file_name_with_empty_url(self):
        url = ""
        result = extract_file_name(url)
        self.assertEqual(result, "")

    def test_extract_file_name_with_none_url(self):
        url = None
        result = extract_file_name(url)
        self.assertEqual(result, "None")

if __name__ == '__main__':
    unittest.main()
