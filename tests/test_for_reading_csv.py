from unittest.mock import patch
from src.reading_csv import read_csv_file
from typing import Any



@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv_file: Any) -> None:
    operations = [
        {
            "id": 4699552,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        }
    ]
    mock_read_csv_file.return_value.to_dict.return_value = operations
    data_from_csv = operations
    assert data_from_csv