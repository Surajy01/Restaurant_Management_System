from app.utils.file_handler import read_data, write_data
from app.utils.logger import write_log
import logging

FOOD_FILE="app/database/food.json"

class UpdateFoodManager:

    def update_food(self):

        try:

            foods=read_data(FOOD_FILE)

            if not foods:
                print("\n❌ No food items available!")
                return

            while True:
                print("\n╔══════════════════════════════════════════════════════╗")
                print("║                 ✏️  UPDATE FOOD ITEM ✏️                ║".center(56))
                print("╠══════════════════════════════════════════════════════╣")

                for index, food in enumerate(foods, 1):
                    row=(
                        f"{index}. {food['name']} "
                        # f"({food.get('food_type', 'N/A')})"
                        f"({food.get('food_type', 'Veg')})"
                        f"[{food['category']}]"
                    )
                    print(f"║ {row.ljust(52)} ║")
                print("║ 0. Exit".ljust(55) + "║")
                print("╚══════════════════════════════════════════════════════╝")

                try:
                    choice=int(input("\nSelect Food Number: "))

                    if choice==0:
                        print("\n↩ Returning to Previous Menu...")
                        return

                    food=foods[choice - 1]

                except (ValueError, IndexError):
                    print("❌ Invalid Choice!")
                    continue

                print("\n╔════════════════════════════════════════════╗")
                print("║           UPDATE FOOD DETAILS              ║")
                print("╚════════════════════════════════════════════╝")
                print("Press Enter to keep existing value.\n")

                # Name
                new_name=input(f"🍽 Old Name ({food['name']})\n➜ New Name: ")
                if new_name.strip():
                    food["name"]=new_name

                # Category
                new_category=input(f"\n📂 Old Category ({food['category']})\n➜ New Category: ")
                if new_category.strip():
                    food["category"]=new_category

                # Food Type
                old_type=food.get("food_type", "Veg")

                print(f"\n🥗 Old Food Type : {old_type}")
                print("1. Veg")
                print("2. Non-Veg")
                print("Press Enter to keep existing")

                food_type_choice=input("➜ Select Food Type: ")

                if food_type_choice == "1":
                    food["food_type"]="Veg"
                elif food_type_choice == "2":
                    food["food_type"]="Non-Veg"

                # # Quantity
                # new_qty=input(f"Old Quantity ({food['quantity']}), New Quantity: ")
                # if new_qty.strip():
                #     food["quantity"]=new_qty

                # Unit
                new_unit=input(f"\n📦 Old Unit ({food['unit']})\n➜ New Unit: ")
                if new_unit.strip():
                    food["unit"]=new_unit

                # Stock
                new_stock=input(f"\n📊 Old Stock ({food['stock']})\n➜ New Stock: ")
                if new_stock.strip():
                    try:
                        food["stock"]=int(new_stock)
                    except ValueError:
                        print("❌ Invalid stock value! Keeping old stock.")

                # Price
                new_price=input(f"\n💰 Old Price (₹{food['price']})\n➜ New Price: ")
                if new_price.strip():
                    try:
                        food["price"]=float(new_price)
                    except ValueError:
                        print("❌ Invalid price value! Keeping old price.")

                write_data(FOOD_FILE, foods)

                write_log(
                f"Food Updated | Name: {food.get('name')} | "
                f"Category: {food.get('category')} | "
                f"Type: {food.get('food_type')} | "
                # f"Updated By: {self.username}"
                )

                print("\n╔════════════════════════════════════════════╗")
                print("║        ✅ FOOD UPDATED SUCCESSFULLY        ║")
                print("╚════════════════════════════════════════════╝")

                print(f"\n🍽 Name      : {food['name']}")
                print(f"📂 Category  : {food['category']}")
                print(f"🥗 Type      : {food.get('food_type', 'Veg')}")
                print(f"📦 Unit      : {food['unit']}")
                print(f"📊 Stock     : {food['stock']}")
                print(f"💰 Price     : ₹{food['price']}")

                input("\nPress Enter to continue...")
                return
            
        except Exception:
            logging.exception("Unexpected error while updating food")
            print("❌ Something went wrong!")

            