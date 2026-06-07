from App.auth.sign_up import signup
from App.auth.sign_in import signin
from App.menu.food_menu import menu_system
from App.menu.customer_menu import customer_menu


def auth_menu():
    while True:
        print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")

        choice=input("Enter Choice: ")

        if choice=="1":
            signup()

        elif choice=="2":
            user=signin()

            if user:
                if user["role"].lower()=="admin":
                    # print("Admin")
                    menu_system()
                elif user["role"].lower()=="staff":
                    print("Staff")
                elif user["role"].lower()=="customer":
                    customer_menu()

        elif choice=="3":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")