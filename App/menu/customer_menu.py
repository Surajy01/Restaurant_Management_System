
def customer_menu(customer):
    while True:
        print("\n┌─────────────────────────────────────┐")
        print("│       👤 CUSTOMER DASHBOARD 👤      │")
        print("├─────────────────────────────────────┤")
        print("│ [1] 🍽️  View Menu                    │")
        print("│ [2] 🛒 Place Order                  │")
        print("│ [3] 💰 Pay Bill                     │")
        print("│ [4] 🪑 Table Booking                │")
        print("│ [5] 📋 My Orders                    │")
        print("│ [6] 🗑️  Cancel Order                 │")
        print("│ [7] 🚪 Exit/Logout                  │")
        print("└─────────────────────────────────────┘")
        # print("7. Update Profile")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            customer.view_food_menu()

        elif choice=="2":
            customer.place_order()

        elif choice=="3":
            order_id=input("Enter Order ID: ")
            customer.Pay_bill(order_id)

        elif choice=="4":
            customer.table_booking()

        elif choice=="5":
            customer.view_orders_history()

        elif choice=="6":
            customer.cancel_order()

        # elif choice=="6":
        #     print("Update Profile")
            
        elif choice=="7":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")
