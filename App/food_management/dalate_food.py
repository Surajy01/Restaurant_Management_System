from app.utils.file_handler import read_data, write_data
from app.utils.logger import write_log
import logging

FOOD_FILE="app/database/food.json"

class DeleteFoodManager:

    def delete_food(self):

        try:

            foods=read_data(FOOD_FILE)

            if not foods:
                logging.error("Delete Food Failed | No food items found")
                print("\n❌ No Food Items Found!")
                return

            print("\n" + "═" * 60)
            print("🗑️ DELETE FOOD ITEM 🗑️".center(60))
            print("═" * 60)

            print("╔════╦══════════════════════╦══════════════╦══════════╗")
            print("║ No ║ Food Name            ║ Category     ║ Type     ║")
            print("╠════╬══════════════════════╬══════════════╬══════════╣")

            for index, food in enumerate(foods, 1):

                print(
                    f"║ {index:<2} "
                    f"║ {food['name'][:20]:<20} "
                    f"║ {food['category'][:12]:<12} "
                    f"║ {food.get('food_type', 'Veg')[:8]:<8} ║"
                )

            print("╚════╩══════════════════════╩══════════════╩══════════╝")

            try:

                choice=int(input("\n👉 Select Food Number to Delete: "))

                if choice < 1 or choice > len(foods):
                    logging.error(f"Delete Food Failed | Invalid Choice: {choice}")
                    print("❌ Invalid Choice!")
                    return

                selected_food=foods[choice - 1]

            except ValueError:

                logging.error("Delete Food Failed | Non-numeric choice entered")

                print("❌ Please enter a valid number!")
                return

            print("\n" + "─" * 50)
            print(f"🍽 Food Name : {selected_food['name']}")
            print(f"📂 Category  : {selected_food['category']}")
            print(f"🥗 Type      : {selected_food.get('food_type', 'Veg')}")
            print("─" * 50)

            confirm=input("\n⚠️ Are you sure you want to delete this item? (y/n): ").lower()

            if confirm != "y":

                write_log(f"Food Delete Cancelled | "
                    f"Food: {selected_food['name']}")

                print("❌ Deletion Cancelled!")
                return

            removed=foods.pop(choice - 1)

            write_data(FOOD_FILE, foods)

            write_log(
                f"Food Deleted Successfully | "
                f"Food: {removed['name']} | "
                f"Category: {removed['category']} | "
                f"Type: {removed.get('food_type', 'Veg')}"
            )

            print("\n" + "═" * 60)
            print("✅ FOOD DELETED SUCCESSFULLY ✅".center(60))
            print("═" * 60)

            print(f"🍽 Name      : {removed['name']}")
            print(f"📂 Category  : {removed['category']}")
            print(f"🥗 Type      : {removed.get('food_type', 'Veg')}")

            print("═" * 60)

        except Exception:
            logging.exception("Unexpected error while deleting food item")
            print("❌ Something went wrong!")

