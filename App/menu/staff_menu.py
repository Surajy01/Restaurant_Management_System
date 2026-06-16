
def staff_menu(staff):
    while True:
        print("\n===== MENU =====")
        print("1. View MENU")
        print("2. Take Order")
        print("3. Table Reservation")
        print("4. Generate Bill")
        print("5. View All Orders")
        print("6. Update Order Status")
        print("7. View Available Foods")
        # print("8. Update Profile")
        # print("9. Logout")
        print("8. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            staff.view_food_menu()
        elif choice=="2":
            staff.take_order()
            # print("Take Order")
        elif choice=="3":
            print("Table Reservation")

        elif choice=="4":
            order_id=input("Enter Order ID: ")
            staff.payment_menus(order_id)
            # print("Generate Bill")

        elif choice=="5":
            staff.view_orders()
        elif choice=="6":
            staff.update_order_status()
        elif choice=="7":
            staff.view_available_foods()
        # elif choice=="8":
        #     print("Update Profile")
        #     break
        # elif choice=="9":
        #     print("Thank You!")
            break
        elif choice=="8":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")