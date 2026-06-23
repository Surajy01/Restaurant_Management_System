from app.services.view_all_orders import ViewAllOrdersServices
from app.services.update_order_status import UpdateOrderStatusServices

def order_management():
    while True:
        print("\n╔═════════════════════════════════════╗")
        print("║      📦 ORDER MANAGEMENT 📦         ║")
        print("╠═════════════════════════════════════╣")
        print("║ 1. 📋 View All Orders               ║")
        print("║ 2. 🔍 Search Order                  ║")
        print("║ 3. 🔄 Update Order Status           ║")
        print("║ 4. ❌ Cancel Order                  ║")
        print("║ 5. 📊 Order Reports                 ║")
        print("║ 6. 🔙 Back                          ║")
        print("╚═════════════════════════════════════╝")

        choice = input("👉 Enter your choice: ")

        if choice=="1":
            ViewAllOrdersServices().view_all_orders()

        elif choice=="2":
            print(" Search Order by id")
            # search_order()

        elif choice=="3":
            UpdateOrderStatusServices().update_order_status()

        elif choice=="4":
            print(" cancel Order by id")
            # cancel_order()

        elif choice=="5":
            print(" Order reports")
            # order_reports()

        elif choice=="6":
            print("🔙 Returning to Previous Dashboard")
            break

        else:
            print("❌ Invalid choice! Please try again.")