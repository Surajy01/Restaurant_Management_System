from App.utils.file_handler import read_data, write_data

def update_food():
    foods=read_data()

    if not foods:
        print("No Food Items Found!")
        return
    
    print("\n===== UPDATE FOOD =====")

    for index, food in enumerate(foods, 1):
        print(f"{index}. {food['name']} ({food['category']})")

    try:
        choice=int(input("Select food to update: "))
        food=foods[choice - 1]
    except(ValueError, IndexError):
        print("Invalid Choice")
        return

    # food["name"] = input("New name: ") or food["name"]
    # food["quantity"] = input("New quantity: ") or food["quantity"]

    # price = input("New price: ")
    # if price:
    #     food["price"] = float(price)

    print("\n===== UPDATE DETAILS =====")

    # Name
    new_name=input(f"Old Name ({food['name']}), New Name: ")
    if new_name.strip():
        food["name"]=new_name

    # Quantity
    new_qty=input(f"Old Quantity ({food['quantity']}), New Quantity: ")
    if new_qty.strip():
        food["quantity"]=new_qty

    # Price
    new_price=input(f"Old Price ({food['price']}), New Price: ")
    if new_price.strip():
        food["price"]=float(new_price)

    write_data(foods)
    print("Food updated successfully!")