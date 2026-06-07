from App.utils.file_handler import read_data, write_data

def delete_food():
    foods=read_data()

    if not foods:
        print("No Food Items Found!")
        return
    
    print("\n===== DELETE FOOD =====")

    for index, food in enumerate(foods, 1):
        print(f"{index}. {food['name']} ({food['category']})")

    try:
        choice=int(input("Select food to delete: "))
        removed=foods.pop(choice - 1)
    except:
        print("Invalid Choice")
        return

    write_data(foods)

    print(f"{removed['name']} deleted successfully!")