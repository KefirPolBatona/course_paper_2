#####

import datetime
from src.utils import list_operations
from src.mod_class import Output


# Список всех выполненных банковских операций
list_operations_executed = []

# Хронологический список выполненных банковских операций
list_operations_chronology = []

# Список операций для вывода на экран
output_operations = []


def operations_executed():
    """
    Добавляет в список все выполненные банковские операции
    """
    for operation in list_operations():
        if not operation:
            pass
        elif operation["state"] != "EXECUTED":
            pass
        elif operation["description"] == "Открытие вклада":
            pass
        else:
            list_operations_executed.append(operation)
    return list_operations_executed

operations_executed()


def operations_chronology(list_operations_executed):
    """
    Сортирует список выполненных банковских операций в хронологическом порядке
    """
    for operation in list_operations_executed:
        operation["date"] = datetime.datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
        if not list_operations_chronology:
            list_operations_chronology.append(operation)
        elif operation["date"] > list_operations_chronology[-1]["date"]:
            list_operations_chronology.append(operation)
        else:
            for operation_chronology in list_operations_chronology:
                if operation["date"] < operation_chronology["date"]:
                    list_operations_chronology.insert(list_operations_chronology.index(operation_chronology), operation)
                    break
                else:
                    continue
    return list_operations_chronology

operations_chronology(list_operations_executed)


def class_output():
    """
    Итерирует 5 последних операций из хронологического списка выполненных банковских операций.
    В каждой итерации извлекает аргументы для экземпляра класса Output.
    Вызывает все функции класса для каждого экземпляра.
    """
    for element in list_operations_chronology[-5:]:
        instance_class = Output(element['id'], element['state'], element['date'], element['operationAmount'],\
                                          element['description'], element['from'], element['to'])
        instance_class.date_conversion()
        instance_class.define_amount()
        instance_class.define_currency_name()
        instance_class.define_from_name()
        instance_class.define_from_number_hidden()
        instance_class.define_to_name()
        instance_class.define_to_number_hidden()

        """ Добавляет новый экземпляр класса в список операций для вывода на экран, в начало списка """
        output_operations.insert(0, instance_class)
    return output_operations

class_output()


def output():
    """
    Выводит на экран список из 5 последних успешных операций
    """
    for element in output_operations:
        print(f"\n{element.date} {element.description} \n"
              f"{element.from_name} {element.from_number_hidden} -> {element.to_name} {element.to_number_hidden}\n"
              f"{element.amount} {element.currency_name}")

output()

##################