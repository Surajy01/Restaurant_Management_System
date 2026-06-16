
def customer_menu(customer):
    while True:
        print("\n===== MENU =====")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View My Orders")
        print("4. Cancel Order")
        print("5. Pay Bill")
        print("6. Table Booking")
        # print("7. Update Profile")
        # print("7. Logout")
        print("7. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            customer.view_food_menu()
        elif choice=="2":
            customer.place_order()
            # print("Order placed successfully.")
        elif choice=="3":
            customer.view_orders()
        elif choice=="4":
            customer.cancel_order()

        elif choice=="5":
            order_id=input("Enter Order ID: ")
            customer.Pay_bill(order_id)

        elif choice=="6":
            customer.table_booking()
        # elif choice=="6":
        #     print("Update Profile")
        # elif choice=="7":
        #     print("Thank You!")
            break
        elif choice=="7":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")