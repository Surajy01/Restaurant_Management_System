from app.services.view_all_staff import ViewAllStaffService

def staff_management():

    while True:
        print("\n╔═════════════════════════════════════╗")
        print("║      👨‍💼 STAFF MANAGEMENT 👨‍💼     ║")
        print("╠═════════════════════════════════════╣")
        print("║ 1. ➕ Add Staff(N/A)                ║")
        print("║ 2. 📋 View All Staff                ║")
        print("║ 3. 🔍 Search Staff(N/A)             ║")
        print("║ 4. ✏️  Update Staff Details(N/A)     ║")
        print("║ 5. ❌ Remove Staff(N/A)             ║")
        print("║ 6. 🔙 Back                          ║")
        print("╚═════════════════════════════════════╝")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            print("Staff member added successfully.")
            # add_staff()

        elif choice=="2":
            ViewAllStaffService("app/database/sign_up.json").view_all_staff()
            # print("Displaying staff members.")

        elif choice=="3":
            print("Search Staff members.")
            # search_staff()

        elif choice=="4":
            print("Update Staff members.")
            # update_staff()

        elif choice=="5":
            print("Staff member removed successfully.")
            # remove_staff()

        elif choice=="6":
            print("🔙 Returning to Previous Dashboard")
            break

        else:
            print("❌ Invalid choice! Please try again.")

