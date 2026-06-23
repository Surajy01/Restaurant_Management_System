
def admin_menu(admin):
    while True:
        print("\n┌───────────────────────────────────────┐")
        print("│         👑 ADMIN DASHBOARD 👑         │")
        print("├───────────────────────────────────────┤")
        print("│ [1] 🍔 Menu Management                │")
        print("│ [2] 📦 Order Management               │")
        print("│ [3] 👨‍💼 Staff Management             │")
        print("│ [4] 📈 Reports & Analytics            │")
        print("│ [5] 🚪 Exit/Logout                    │")
        print("└───────────────────────────────────────┘")
        # print("2. View All Orders")
        # print("3. Update Order Status")
        # print("10. View Sales Report")
        # print("11. Update Profile")
        # print("12. Logout")

        choice=input("👉 Enter your choice: ")

        # if choice=="1":
        #     admin.view_food_menu()

        # elif choice=="2":
        #     admin.add_food()

        # elif choice=="3":
        #     admin.update_food()

        # elif choice=="4":
        #     admin.delete_food()
        if choice=="1":
            admin.menu_management()

        elif choice=="2":
            admin.order_management()
            # admin.view_all_orders()
        
        elif choice=="3":
            admin.staff_management()

        elif choice=="4":
            admin.reports_menu()

        # elif choice=="3":
        #     admin.update_order_status()

        # elif choice=="3":
        #     admin.view_staff()

        # elif choice=="4":
        #     admin.add_staff()

        # elif choice=="5":
        #     admin.remove_staff()

        # elif choice=="10":
        #     print("View Sales Report")

        # elif choice=="11":
        #     print("Update Profile")

        # elif choice=="12":
        #     print("Thank You!")

        elif choice=="5":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")