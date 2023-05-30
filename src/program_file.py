#####

import datetime

from utils import list_operations

# Список всех выполненных банковских операций
list_operations_executed = []
# Хронологический список выполненных банковских операций
list_operations_chronology = []


""" Добавляет в список все выполненные банковские операции """
for operation in list_operations():
    if not operation:
        pass
    elif operation["state"] != "EXECUTED":
        pass
    elif operation["description"] == "Открытие вклада":
        pass
    else:
        list_operations_executed.append(operation)


""" Сортирует список выполненных банковских операций в хронологическом порядке """
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


# for element in list_operations_chronology:
#     print(element)







