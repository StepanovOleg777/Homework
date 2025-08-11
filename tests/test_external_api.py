import unittest
from unittest.mock import patch
from src.external_api import transaction_amount

class TestTransactionAmount(unittest.TestCase):

    @patch('requests.get')
    def test_usd_conversion(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 75.0}

        transaction = [{
            "operationAmount": {
                "amount": "1",
                "currency": {"code": "USD"}
            }
        }]

        result = transaction_amount(transaction)
        self.assertEqual(result, 75.0)

    @patch('requests.get')
    def test_no_transaction(self, mock_get):
        transaction = [{}]
        result = transaction_amount(transaction)
        self.assertEqual(result, "Нет транзакции!")

if __name__ == '__main__':
    unittest.main()
