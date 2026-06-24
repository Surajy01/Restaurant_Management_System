from app.services.view_all_orders import ViewAllOrdersServices
from app.services.update_order_status import UpdateOrderStatusServices
from app.order.cancel_order import CancelOrder


def order_management(user):
    while True:
        print("\n╔═════════════════════════════════════╗")
        print("║      📦 ORDER MANAGEMENT 📦         ║")
        print("╠═════════════════════════════════════╣")
        print("║ 1. 📋 View All Orders               ║")
        print("║ 2. 🔍 Search Order(N/A)             ║")
        print("║ 3. 🔄 Update Order Status           ║")
        print("║ 4. ❌ Cancel Order                  ║")
        # print("║ 5. 📊 Order Reports                 ║")
        print("║ 5. 🔙 Back                          ║")
        print("╚═════════════════════════════════════╝")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            ViewAllOrdersServices().view_all_orders()

        elif choice=="2":
            print(" Search Order by id")
            # search_order()

        elif choice=="3":
            UpdateOrderStatusServices().update_order_status()

        elif choice=="4":
            order_id=input("Enter Order ID to Cancel: ").strip()

            CancelOrder(
                customer_name=user.username,
                order_id=order_id,
                role=user.role
            ).execute()

        # elif choice=="5":
        #     print(" Order reports")
            # order_reports()

        elif choice=="5":
            print("🔙 Returning to Previous Dashboard")
            break

        else:
            print("❌ Invalid choice! Please try again.")

            