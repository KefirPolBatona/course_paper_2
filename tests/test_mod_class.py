import pytest
import datetime
# from src import mod_class
from src.mod_class import Output

@pytest.fixture
def coll():
    return Output(441945886, "EXECUTED", datetime.datetime(2018, 1, 13, 13, 0, 58, 458625),\
                           {"amount": "31957.58","currency": {"name": "руб.", "code": "RUB"}},\
                           "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589")


class TestOutput():
    """Тест для класса Output"""

    def test_date_conversion(self, coll):
        """
        Проверяет тип аргумента date
        """
        instance_class = coll
        assert isinstance(instance_class.date_conversion(), str)


    def test_define_amount(self, coll):
        """
        Проверяет значение аргумента amount
        """
        instance_class = coll
        assert float(instance_class.define_amount()) == 31957.58


    def test_define_currency_name(self, coll):
        """
        Проверяет значение аргумента currency_name
        """
        instance_class = coll
        assert instance_class.define_currency_name() == "руб."


    def test_define_from_name(self, coll):
        """
        Проверяет значение аргумента from_name
        """
        instance_class = coll
        assert instance_class.define_from_name() == "Maestro"


    def test_define_from_number_hidden(self, coll):
        """
        Проверяет количество "*" в аргументе from_number_hidden
        """
        instance_class = coll
        assert instance_class.define_from_number_hidden().count("*") == 6


    def test_define_to_name(self, coll):
        """
        Проверяет значение аргумента to_name
        """
        instance_class = coll
        assert instance_class.define_to_name() == "Счет"


    def test_define_to_number_hidden(self, coll):
        """
        Проверяет последние 4 символа в значении аргумента to_number_hidden
        """
        instance_class = coll
        assert int(instance_class.define_to_number_hidden()[-4:]) == 9589
