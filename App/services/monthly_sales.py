from collections import defaultdict
from datetime import datetime
from app.utils.file_handler import read_data
import logging


class MonthlySalesReportService:

    def __init__(self, order_file):
        self.order_file=order_file

    def show_monthly_sales_report(self):

        try:

            orders=read_data(self.order_file)

            if not orders:
                print("❌ No Orders Found!")
                return

            monthly_sales=defaultdict(float)
            monthly_orders=defaultdict(int)

            for order in orders:

                try:
                    order_date=datetime.strptime(
                        order["order_date"],
                        "%d-%m-%Y"
                    )

                    month_year=order_date.strftime("%B %Y")

                    monthly_sales[month_year] += order.get(
                        "final_total",
                        0
                    )

                    monthly_orders[month_year] += 1

                except Exception:
                    continue

            print("\n" + "═" * 75)
            print("📊 MONTHLY SALES REPORT 📊".center(75))
            print("═" * 75)

            print(
                f"{'Month':<20}"
                f"{'Orders':<15}"
                f"{'Revenue'}"
            )

            print("─" * 75)

            for month, revenue in monthly_sales.items():

                print(
                    f"{month:<20}"
                    f"{monthly_orders[month]:<15}"
                    f"₹{revenue:.2f}"
                )

            print("═" * 75)

        except Exception:

            logging.exception("Error While Generating Monthly Sales Report")

            print("❌ Something went wrong!")

