from app.utils.file_handler import read_data
from app.utils.logger import write_log
import logging

FOOD_FILE="app/database/food.json"

class ViewFoodManager:

    def view_food_menu(self):

        try:

            foods=read_data(FOOD_FILE)

            categories=["Starters", "Breakfast", "Main Course", "Desserts", "Beverages"]

            print("\n" + "═" * 66)
            print("🍽  RESTAURANT FOOD MENU 🍽".center(66))
            print("═" * 66)

            for category in categories:

                print("\n")
                print(f" {category.upper()} ".center(66, "═"))

                # Categories that should be separated into Veg and Non-Veg
                if category in ["Starters", "Breakfast", "Main Course"]:

                    for food_type in ["Veg", "Non-Veg"]:

                        print(f"\n{'🟢' if food_type=='Veg' else '🔴'} {food_type.upper()} ITEMS".center(66))

                        print("╔══════════════════════╦══════════════╦════════════╦════════════╗")
                        print("║ Food Name            ║ Unit         ║ Stock      ║ Price      ║")
                        print("╠══════════════════════╬══════════════╬════════════╬════════════╣")

                        found=False

                        for food in foods:

                            if (
                                food["category"]==category
                                and food.get("food_type")==food_type
                            ):

                                stock=str(food["stock"]) if food["stock"] > 0 else "Out"

                                print(
                                    f"║ {food['name'][:20]:<20} "
                                    f"║ {food['unit'][:12]:<12} "
                                    f"║ {stock:<10} "
                                    f"║ ₹{food['price']:<10}║"
                                )

                                found=True

                        if not found:
                            print("║{:^66}║".format("No Items Found"))

                        print("╚══════════════════════╩══════════════╩════════════╩════════════╝")

                else:
                    # Desserts and Beverages
                    print("╔══════════════════════╦══════════════╦════════════╦════════════╗")
                    print("║ Food Name            ║ Unit         ║ Stock      ║ Price      ║")
                    print("╠══════════════════════╬══════════════╬════════════╬════════════╣")

                    found=False

                    for food in foods:

                        if food["category"]==category:

                            stock=str(food["stock"]) if food["stock"] > 0 else "Out"

                            print(
                                f"║ {food['name'][:20]:<20} "
                                f"║ {food['unit'][:12]:<12} "
                                f"║ {stock:<10} "
                                f"║ ₹{food['price']:<10}║"
                            )

                            found=True

                    if not found:
                        print("║{:^66}║".format("No Items Found"))

                    print("╚══════════════════════╩══════════════╩════════════╩════════════╝")

            print("\n" + "═" * 66)
            write_log(f"Food Menu Viewed Successfully | Total Foods: {len(foods)}")

        except Exception:
            logging.exception("Unexpected error while viewing food menu")
            print("❌ Unable to display food menu!")


