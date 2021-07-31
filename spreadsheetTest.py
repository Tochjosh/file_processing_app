import unittest

from processSpreadSheet import SpreadSheet


class TestSpreadSheet(unittest.TestCase):
    def setUp(self):
        self.sheet = SpreadSheet()

    def test_read_all_contents(self):
        file = self.sheet.read_all_content('data.csv')
        self.assertIsNotNone(file, True)

        file = self.sheet.read_all_content('values.tsv')
        self.assertIsNotNone(file, True)

        file = self.sheet.read_all_content('data.csv')
        length = len(file)
        self.assertGreater(length, 0)

    def test_read_first_two_lines(self):
        file = self.sheet.read_first_two_lines('data.csv')
        self.assertIsNotNone(file, True)

        file = self.sheet.read_first_two_lines('values.tsv')
        self.assertIsNotNone(file, True)

        file = self.sheet.read_first_two_lines('data.csv')
        length = len(file)
        self.assertGreater(length, 0)

    def test_read_last_two_lines(self):
        file = self.sheet.read_last_two_lines('data.csv')
        self.assertIsNotNone(file, True)

        file = self.sheet.read_last_two_lines('values.tsv')
        self.assertIsNotNone(file, True)

        file = self.sheet.read_last_two_lines('data.csv')
        length = len(file)
        self.assertGreater(length, 0)


if __name__ == '__main__':
    unittest.main()
