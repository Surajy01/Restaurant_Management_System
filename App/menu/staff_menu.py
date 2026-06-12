
def staff_menu(staff):
    while True:
        print("\n===== MENU =====")
        print("1. View MENU")
        # print("2. Place Order")
        print("2. View All Orders")
        print("3. Update Order Status")
        print("4. Generate Bill")
        print("5. View Available Foods")
        # print("7. Update Profile")
        # print("8. Logout")
        print("6. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            staff.view_food_menu()
        # elif choice=="2":
        #     print("Place Order")
        elif choice=="2":
            staff.view_orders()
        elif choice=="3":
            staff.update_order_status()
        elif choice=="4":
            print("Generate Bill")
        elif choice=="5":
            staff.view_available_foods()
        # elif choice=="7":
        #     print("Update Profile")
        #     break
        # elif choice=="8":
        #     print("Thank You!")
            break
        elif choice=="6":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")