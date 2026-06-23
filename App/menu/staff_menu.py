
def staff_menu(staff):
    while True:
        print("\n┌────────────────────────────────────────┐")
        print("│        👨‍🍳 STAFF DASHBOARD 👨‍🍳       │")
        print("├────────────────────────────────────────┤")
        print("│ [1] 📋 View Menu                       │")
        print("│ [2] 🛒 Take Order                      │")
        print("│ [3] 🪑 Table Reservation               │")
        print("│ [4] 🧾 Generate Bill                   │")
        print("│ [5] 📦 Manage Orders                   │")
        # print("│ [6] 🍽️ View Available Foods          │")
        print("│ [6] 🚪 Exit/Logout                     │")
        print("└────────────────────────────────────────┘")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            staff.view_food_menu()

        elif choice=="2":
            staff.take_order()

        elif choice=="3":
            staff.table_reservation()

        elif choice=="4":
            order_id=input("Enter Order ID: ")
            staff.payment_menus(order_id)

        elif choice=="5":
            staff.order_management()

        # elif choice=="5":
        #     staff.view_orders()

        # elif choice=="6":
        #     staff.update_order_status()

        # elif choice=="7":
        #     staff.view_available_foods()

        # elif choice=="8":
        #     print("Update Profile")
        #     break
        
        # elif choice=="9":
        #     print("Thank You!")
            # break

        elif choice=="6":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")