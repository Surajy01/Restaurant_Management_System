from app.utils.file_handler import read_data
import logging


class RevenueAnalysisService:

    def __init__(self, order_file):
        self.order_file=order_file

    def _load_orders(self):
        try:
            orders=read_data(self.order_file)
            return orders if orders else []
        except Exception:
            logging.exception("Failed to load orders for revenue analytics")
            return []

    def show_revenue_dashboard(self):

        try:

            orders=self._load_orders()

            if not orders:
                print("❌ No Orders Found!")
                return

            total_revenue=0
            paid_revenue=0
            pending_revenue=0

            paid_orders=0

            for order in orders:

                amount=order.get("final_total", 0)
                total_revenue += amount

                if order.get("payment_status") == "Paid":
                    paid_revenue += amount
                    paid_orders += 1
                else:
                    pending_revenue += amount

            total_orders=len(orders)
            avg_order_value=total_revenue / total_orders if total_orders else 0

            print("\n" + "═" * 60)
            print("💰 REVENUE ANALYTICS DASHBOARD 💰".center(60))
            print("═" * 60)

            print(f"📦 Total Orders        : {total_orders}")
            print(f"💰 Total Revenue       : ₹{total_revenue:.2f}")
            print(f"✅ Paid Revenue        : ₹{paid_revenue:.2f}")
            print(f"⏳ Pending Revenue     : ₹{pending_revenue:.2f}")
            print(f"📊 Avg Order Value     : ₹{avg_order_value:.2f}")

            print("\n" + "─" * 60)

            if total_revenue > 0:

                print(f"💳 Paid %              : {(paid_revenue / total_revenue) * 100:.2f}%")
                print(f"⏳ Pending %           : {(pending_revenue / total_revenue) * 100:.2f}%")

            print("═" * 60)

        except Exception:

            logging.exception("Error in Revenue Analytics Dashboard")
            print("❌ Something went wrong!")


            