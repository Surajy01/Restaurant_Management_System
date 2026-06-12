from App.utils.file_handler import read_data

FOOD_FILE="App/database/foods.json"

class ViewFoodManager:

    def view_food_menu(self):

        foods=read_data(FOOD_FILE)

        categories=["Starters", "Breakfast", "Lunch", "Dinner"]
        for category in categories:
            print("\n" + f" {category.upper()} MENU ".center(60, "="))
            print()
            print("-" * 60)
            print(f"{'Food Name':<20}{'Unit':<15}{'Stock':<15}{'Price'}")
            print("-" * 60)
            found=False

            for food in foods:
                if food["category"]==category:
                    print(f"{food['name']:<20}{food['unit']:<15}{food['stock']:<15}₹{food['price']}")
                    found=True

            if not found:
                print("No Items Found")
            print("-" * 60)

        # if not foods:
        #     print("No food items available!")
        #     return
        # for food in foods:
        #     print(f"ID: {food['id']}")
        #     print(f"Name: {food['name']}")
        #     print(f"Category: {food['category']}")
        #     print(f"Unit: {food['unit']}")
        #     print(f"Stock: {food['stock']}")
        #     print(f"Price: ${food['price']:.2f}")
        #     print("-"*20)