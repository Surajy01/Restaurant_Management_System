import uuid
from App.utils.file_handler import read_data, write_data

def add_food():
    print("\n===== FOOD MENU CATEGORY =====")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")

    choice=input("Select Category: ")

    category_map={
        "1": "Breakfast",
        "2": "Lunch",
        "3": "Dinner"
    }

    if choice not in category_map:
        print("Invalid Choice!")
        return

    category=category_map[choice]

    food={
        "id": str(uuid.uuid4())[:8],
        "category": category,
        "name": input("Enter Food Name: "),
        "quantity": input("Enter Quantity: "),
        "price": float(input("Enter Price: "))
    }

    foods=read_data()
    foods.append(food)
    write_data(foods)

    print(f"{food['name']} added successfully!")