import uuid
from app.utils.file_handler import read_data, write_data
from app.domain.food import Food

FOOD_FILE="app/database/food.json"

class AddFoodManager:

    def add_food(self):
        print("\n===== FOOD MENU CATEGORY =====")
        print("1. Starters")
        print("2. Breakfast")
        print("3. Main Course")
        print("4. Desserts")
        print("5. Beverages")
        # print("3. Lunch")
        # print("4. Dinner")

        choice=input("Select Category: ")

        categories={
            "1": "Starters",
            "2": "Breakfast",
            "3": "Main Course",
            "4": "Desserts",
            "5": "Beverages",
            # "3": "Lunch",
            # "4": "Dinner"
        }

        if choice not in categories:
            print("Invalid Choice!")
            return
        
        while True:
            food_type=input("Enter Food Type (Veg/Non-Veg): ").strip()

            if food_type in ["Veg", "Non-Veg"]:
                break

            print("Invalid food type. Enter Veg or Non-Veg.")

        food=Food(
            id=str(uuid.uuid4().hex[:8]),
            category=categories[choice],
            name=input("Enter Food Name: "),
            food_type=food_type,
            unit=input("Enter Unit (Full Plate/Half Plate/Piece/Bowl/Ml): "),
            stock=int(input("Enter Available Stock: ")),
            price=float(input("Enter Price: "))
        )

        foods=read_data(FOOD_FILE)
        foods.append(food.dict())
        write_data(FOOD_FILE,foods)

        print(f"{food.name} added successfully!")
