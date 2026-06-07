from App.food_menu.view_food import view_food_menu


def customer_menu():
    while True:
        print("\n===== MENU =====")
        print("1. View Food MENU")
        print("2. Place Order")
        print("3. Logout")
        print("4. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            view_food_menu()
        elif choice=="2":
            print("Place Order")
        elif choice=="3":
            print("Logout")
        elif choice=="4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")