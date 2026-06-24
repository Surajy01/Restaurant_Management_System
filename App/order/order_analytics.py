from collections import Counter
from app.utils.file_handler import read_data
import logging


class OrderAnalyticsService:

    def __init__(self, order_file):
        self.order_file=order_file

    def _load_orders(self):
        """Private method to load orders safely"""

        try:
            orders=read_data(self.order_file)

            if orders is None:
                return []

            return orders

        except Exception as e:
            logging.exception(f"Failed to load orders from {self.order_file}")
            return []

    def _calculate_status(self, orders):
        """Private method for calculations"""

        status_counts=Counter(order["status"] for order in orders)

        delivered=status_counts.get("Delivered", 0)
        pending=(
            status_counts.get("Pending", 0)
            + status_counts.get("Preparing", 0)
            + status_counts.get("Ready", 0)
        )
        cancelled=status_counts.get("Cancelled", 0)

        return delivered, pending, cancelled

    def show_orderanalytics_dashboard(self):

        try:

            orders=self._load_orders()

            if not orders:
                print("❌ No Orders Found!")
                return

            delivered, pending, cancelled=self._calculate_status(orders)

            total=len(orders)

            print("\n" + "═" * 60)
            print("📊 ORDER ANALYTICS DASHBOARD 📊".center(60))
            print("═" * 60)

            print(f"📦 Total Orders   : {total}")
            print(f"🚚 Delivered      : {delivered}")
            print(f"⏳ Pending/Active  : {pending}")
            print(f"❌ Cancelled      : {cancelled}")

            print("\n" + "─" * 60)

            if total > 0:
                print(f"📈 Delivered %     : {(delivered / total) * 100:.2f}%")
                print(f"📉 Pending %       : {(pending / total) * 100:.2f}%")
                print(f"🚫 Cancelled %     : {(cancelled / total) * 100:.2f}%")

            print("═" * 60)

        except Exception:

            logging.exception("Error in Order Analytics Dashboard")
            print("❌ Something went wrong!")

