import pytest
import datetime
from src.main import operations_executed, operations_chronology


@pytest.fixture
def coll():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }]


def test_operations_executed():
    """
    Проверяет тип operations_executed()
    """
    assert isinstance(operations_executed(), list)


def test_operations_chronology(coll):
    """
    Проверяет, что список, полученный функцией operations_chronology(list_operations_executed), не пуст.
    """
    list_operations_executed = coll
    assert len(operations_chronology(list_operations_executed)) > 0


def test_operations_chronology_a(coll):
    """
    Проверяет, соответствует ли значение 'date' итоговому.
    """
    list_operations_executed = coll
    date = operations_chronology(list_operations_executed)
    assert date[-1]['date'] == datetime.datetime(2019, 12, 7, 6, 17, 14, 634890)



