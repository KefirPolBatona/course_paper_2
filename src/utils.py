import json
from pathlib import Path

def list_operations():
    """
    Загружает список банковских операций
    """
    with open(Path(__file__).parent.parent / 'data' / 'operations.json', encoding="utf-8") as file:

    # with open("../data/operations.json", encoding="utf-8") as file:
        return json.load(file)

