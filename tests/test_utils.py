import unittest
from unittest.mock import mock_open, patch
from src.utils import input_transaction

class TestInputTransaction(unittest.TestCase):

    def test_valid_data(self):
        mock_data = '[{"id": 1, "amount": 100}]'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = input_transaction("path/to/mockfile.json")
            self.assertEqual(result, [{"id": 1, "amount": 100}])

    def test_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = input_transaction("path/to/mockfile.json")
            self.assertEqual(result, [])

    def test_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = input_transaction("path/to/mockfile.json")
            self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
