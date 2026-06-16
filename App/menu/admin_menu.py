
def admin_menu(admin):
    while True:
        print("\n===== MENU =====")
        print("1. View Food")
        print("2. Add Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. View All Orders")
        print("6. Update Order Status")
        print("7. View Staff")
        print("8. Add Staff")
        print("9. Remove Staff")
        # print("10. View Sales Report")
        # print("11. Update Profile")
        # print("12. Logout")
        print("10. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            admin.view_food_menu()

        elif choice=="2":
            admin.add_food()

        elif choice=="3":
            admin.update_food()

        elif choice=="4":
            admin.delete_food()

        elif choice=="5":
            admin.view_all_orders()

        elif choice=="6":
            admin.update_order_status()

        elif choice=="7":
            admin.view_staff()

        elif choice=="8":
            admin.add_staff()

        elif choice=="9":
            admin.remove_staff()

        # elif choice=="10":
        #     print("View Sales Report")

        # elif choice=="11":
        #     print("Update Profile")

        # elif choice=="12":
        #     print("Thank You!")

        elif choice=="10":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")