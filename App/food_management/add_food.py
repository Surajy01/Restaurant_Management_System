import uuid
from app.utils.file_handler import read_data, write_data
from app.domain.food import Food
from app.utils.logger import write_log
import logging

FOOD_FILE="app/database/food.json"

class AddFoodManager:

    def add_food(self):

        try:

            print("\n" + "═" * 50)
            print("🍽 ADD FOOD ITEM 🍽".center(50))
            print("═" * 50)

            print("╔══════════════════════════════════════════════╗")
            print("║  1. 🍢 Starters                              ║")
            print("║  2. 🥞 Breakfast                             ║")
            print("║  3. 🍛 Main Course                           ║")
            print("║  4. 🍨 Desserts                              ║")
            print("║  5. 🥤 Beverages                             ║")
            print("║  6. 🔙 Back                                  ║")
            print("╚══════════════════════════════════════════════╝")

            choice=input("\n👉 Select Category: ").strip()

            categories={
                "1": "Starters",
                "2": "Breakfast",
                "3": "Main Course",
                "4": "Desserts",
                "5": "Beverages"
            }

            if choice=="6":
                return

            if choice not in categories:
                logging.error(f"Invalid category selected: {choice}")
                print("❌ Invalid Choice!")
                return

            while True:

                food_type=input("🥗 Enter Food Type (Veg/Non-Veg): ").strip().title()

                if food_type in ["Veg", "Non-Veg"]:
                    break

                logging.error(f"Invalid food type entered: {food_type}")
                print("❌ Invalid Food Type! Enter Veg or Non-Veg.")

            food_name=input("🍽 Enter Food Name: ").strip().title()

            unit=input("📦 Enter Unit (Full Plate/Half Plate/Piece/Bowl/Ml): ").strip().title()

            try:
                stock=int(input("📊 Enter Available Stock: "))
                price = float(input("💰 Enter Price: ").replace("₹", ""))

            except ValueError:
                logging.error(f"Invalid stock or price entered for {food_name}")
                print("❌ Stock and Price must be numeric!")
                return

            if stock <= 0:
                logging.error(f"Invalid stock entered: {stock}")
                print("❌ Stock must be greater than 0!")
                return

            if price <= 0:
                logging.error(f"Invalid price entered: {price}")
                print("❌ Price must be greater than 0!")
                return

            foods=read_data(FOOD_FILE)

            # Duplicate Check
            for food in foods:

                if (food["name"].lower()==food_name.lower()
                    and food["category"]==categories[choice]
                    and food["food_type"]==food_type
                ):

                    logging.error(
                        f"Duplicate food item attempt: "
                        f"{food_name} | Category: {categories[choice]}"
                    )

                    print("❌ Food Item Already Exists!")
                    return

            new_food=Food(
                id=str(uuid.uuid4().hex[:8]),
                category=categories[choice],
                name=food_name,
                food_type=food_type,
                unit=unit,
                stock=stock,
                price=price
            )

            foods.append(new_food.dict())
            write_data(FOOD_FILE, foods)

            # Success Log
            write_log(
                f"Food Added Successfully | "
                f"Food: {food_name} | "
                f"Category: {categories[choice]} | "
                f"Type: {food_type} | "
                f"Stock: {stock} | "
                f"Price: ₹{price}"
            )

            print("\n" + "═" * 50)
            print("✅ FOOD ADDED SUCCESSFULLY ✅".center(50))
            print("═" * 50)

            print(f"🍽 Name      : {food_name}")
            print(f"📂 Category  : {categories[choice]}")
            print(f"🥗 Type      : {food_type}")
            print(f"📦 Unit      : {unit}")
            print(f"📊 Stock     : {stock}")
            print(f"💰 Price     : ₹{price}")

            print("═" * 50)

        except Exception:
            logging.exception("Unexpected error while adding food")
            print("❌ Something went wrong!")

