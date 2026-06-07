import json
import os

FILE_PATH = "App/database/foods.json"

def read_data():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []

def write_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)