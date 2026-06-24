from app.services.table_services import TableService

def table_menu(customer_name):

    while True:

        print("\n" + "═" * 50)
        print("🪑 TABLE RESERVATION MENU 🪑".center(50))
        print("═" * 50)

        print("╔══════════════════════════════════════════╗")
        print("║  1. 🪑 Reserve Table                     ║")
        print("║  2. 📋 View My Bookings                  ║")
        print("║  3. ❌ Cancel Booking                    ║")
        print("║  4. 🔙 Back                              ║")
        print("╚══════════════════════════════════════════╝")

        print("═" * 50)

        choice=input("\n👉 Select Choice: ")

        if choice=="1":
            TableService().reserve_table(customer_name)

        elif choice=="2":
            TableService().view_my_bookings(customer_name)

        elif choice=="3":
            TableService().cancel_booking(customer_name)

        elif choice=="4":
            print("Returning to Previous Dashboard")
            break

        else:
            print("❌ Invalid Choice!")