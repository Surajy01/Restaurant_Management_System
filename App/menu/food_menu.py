from App.food_menu.add_food import add_food
from App.food_menu.view_food import view_food_menu
from App.food_menu.update_food import update_food
from App.food_menu.delete_food import delete_food

def menu_system():
    while True:
        print("\n===== MENU SYSTEM =====")
        print("1. Add Food")
        print("2. View Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            add_food()

        elif choice=="2":
            view_food_menu()

        elif choice=="3":
            update_food()

        elif choice=="4":
            delete_food()

        elif choice=="5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")