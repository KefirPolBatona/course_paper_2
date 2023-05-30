import json

def list_operations():
    """
    Loads a list of banking transactions
    """
    with open("../data/operations.json", encoding="utf-8") as file:
        return json.load(file)

