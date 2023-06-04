import json

def list_operations():
    """
    Загружает список банковских операций
    """
    with open("../data/operations.json", encoding="utf-8") as file:
        return json.load(file)

