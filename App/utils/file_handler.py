import json
import os

# FILE_PATH = "App/database/food.json"

def read_data(FILE_PATH):
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []

def write_data(FILE_PATH, data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)