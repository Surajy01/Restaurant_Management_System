from app.utils.file_handler import read_data, write_data
from app.utils.logger import write_log
import logging

ORDER_FILE="app/database/orders.json"

class UpdateOrderStatusServices:

    def update_order_status(self):

        try:

            orders=read_data(ORDER_FILE)

            if not orders:
                print("❌ No Orders Found!")
                return

            print("\n" + "═" * 70)
            print("📦 ORDER STATUS MANAGEMENT 📦".center(70))
            print("═" * 70)

            print("┌────┬────────────────┬────────────────────┬──────────────┐")
            print("│ No │ Order ID       │ Customer           │ Status       │")
            print("├────┼────────────────┼────────────────────┼──────────────┤")

            for index, order in enumerate(orders, start=1):

                print(
                    f"│ {index:<2} "
                    f"│ {order['order_id']:<14} "
                    f"│ {order['customer_name'][:18]:<18} "
                    f"│ {order['status']:<12} │"
                )

            print("└────┴────────────────┴────────────────────┴──────────────┘")

            try:
                choice=int(input("\n👉 Select Order Number: "))
                selected_order=orders[choice - 1]

            except (ValueError, IndexError):

                logging.error("Invalid Order Selection in Update Order Status")
                print("❌ Invalid Choice!")
                return

            print("\n" + "═" * 50)
            print("🔄 UPDATE ORDER STATUS 🔄".center(50))
            print("═" * 50)

            print("1. 🟡 Preparing")
            print("2. 🍽 Ready")
            print("3. 🚚 Delivered")
            print("4. ❌ Cancelled")

            status_choice=input("\n👉 Select Status: ").strip()

            status_map={
                "1": "Preparing",
                "2": "Ready",
                "3": "Delivered",
                "4": "Cancelled"
            }

            new_status=status_map.get(status_choice)

            if not new_status:

                logging.error("Invalid Status Choice in Order Update")
                print("❌ Invalid Status!")
                return

            old_status=selected_order["status"]
            selected_order["status"]=new_status

            write_data(ORDER_FILE, orders)

            write_log(f"Order Status Updated | "
                f"Order ID: {selected_order['order_id']} | "
                f"Customer: {selected_order['customer_name']} | "
                f"{old_status} → {new_status}"
            )

            print("\n" + "═" * 50)
            print("✅ ORDER STATUS UPDATED SUCCESSFULLY".center(50))
            print("═" * 50)
            print(f"🆔 Order ID : {selected_order['order_id']}")
            print(f"👤 Customer : {selected_order['customer_name']}")
            print(f"📦 Status   : {new_status}")
            print("═" * 50)

        except Exception:

            logging.exception("Unexpected error while updating order status")
            print("❌ Something went wrong!")

