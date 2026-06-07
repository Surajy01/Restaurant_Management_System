from App.utils.file_handler import read_data

def view_food_menu():
    foods = read_data()

    categories = ["Breakfast", "Lunch", "Dinner"]

    for category in categories:
        print(f"\n===== {category.upper()} MENU =====")
        print("-" * 45)
        print(f"{'Food Name':<20}{'Quantity':<15}{'Price'}")
        print("-" * 45)

        found=False

        for food in foods:
            if food["category"]==category:
                print(f"{food['name']:<20}{food['quantity']:<15}₹{food['price']}")
                found=True

        if not found:
            print("No Items Found")
        
        print("-" * 45)