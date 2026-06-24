
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
        # print("11. Update Profile")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            admin.menu_management()

        elif choice=="2":
            admin.order_management()
            # admin.view_all_orders()
        
        elif choice=="3":
            admin.staff_management()

        elif choice=="4":
            admin.reports_menu()

        # elif choice=="11":
        #     print("Update Profile")

        elif choice=="5":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")
