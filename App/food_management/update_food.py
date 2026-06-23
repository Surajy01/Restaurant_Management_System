from app.utils.file_handler import read_data, write_data

FOOD_FILE="app/database/food.json"

class UpdateFoodManager:

    def update_food(self):

        foods=read_data(FOOD_FILE)
        if not foods:
            print("No food items available!")
            return
        
        print("\n===== UPDATE FOOD ITEM =====")

        for index, food in enumerate(foods, 1):
            print(f"{index}. {food['name']} ({food['category']})")

        try:
            choice=int(input("Select food to update: "))
            food=foods[choice - 1]
        except(ValueError, IndexError):
            print("Invalid Choice")
            return
        
        print("\n===== UPDATE DETAILS =====")
        print("Press Enter to keep existing value.\n")

        # Name
        new_name=input(f"Old Name ({food['name']}), New Name: ")
        if new_name.strip(): #strip used to check if user entered only spaces
            food["name"]=new_name

        # # Quantity
        # new_qty=input(f"Old Quantity ({food['quantity']}), New Quantity: ")
        # if new_qty.strip():
        #     food["quantity"]=new_qty

        # Unit
        new_unit=input(f"Old Unit ({food['unit']}), New Unit: ")
        if new_unit.strip():
            food["unit"]=new_unit

        # Stock
        new_stock=input(f"Old Stock ({food['stock']}), New Stock: ")
        if new_stock.strip(): 
            try:
                food["stock"]=int(new_stock)
            except ValueError:
                print("Invalid stock value! Keeping old stock.")

        # Price
        new_price=input(f"Old Price ({food['price']}), New Price: ")
        if new_price.strip():
            try:
                food["price"]=float(new_price)
            except ValueError:
                print("Invalid price value! Keeping old price.")

        write_data(FOOD_FILE,foods)
        print(f"{food['name']} updated successfully!")

