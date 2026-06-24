from app.utils.file_handler import read_data, write_data
from app.utils.logger import write_log
import logging

ORDER_FILE="app/database/orders.json"

class CancelOrder:

    def __init__(self, customer_name, order_id,role):
        self.customer_name=customer_name
        self.order_id=order_id
        self.role=role

    def execute(self):

        try:

            orders=read_data(ORDER_FILE)

            # Admin/Staff can cancel any order
            if self.role.lower() in ["admin", "staff"]:

                for order in orders:

                    if order["order_id"]==self.order_id:

                        if order["status"] in ["Delivered", "Cancelled"]:

                            logging.error(
                                f"Cancel Order Failed | "
                                f"Role: {self.role} | "
                                f"User: {self.customer_name} | "
                                f"Order ID: {self.order_id} | "
                                f"Status: {order['status']}"
                            )

                            print(
                                f"❌ Order ID {self.order_id} cannot be cancelled "
                                f"because it is already {order['status']}."
                            )
                            return

                        order["status"]="Cancelled"

                        write_data(ORDER_FILE, orders)

                        write_log(
                            f"Order Cancelled | "
                            f"Order ID: {self.order_id} | "
                            f"Cancelled By: {self.customer_name} ({self.role})"
                        )

                        print("✅ Order Cancelled Successfully!")
                        return

                print("❌ Order ID not found!")
                return

            # Customer can cancel only own orders
            customer_orders=[
                order for order in orders
                if order["customer_name"]==self.customer_name
            ]

            if not customer_orders:

                print("❌ You have no orders.")
                return

            for order in customer_orders:

                if order["order_id"]==self.order_id:

                    if order["status"] in ["Delivered", "Cancelled"]:

                        print(
                            f"❌ Order ID {self.order_id} cannot be cancelled "
                            f"because it is already {order['status']}."
                        )
                        return

                    order["status"]="Cancelled"

                    write_data(ORDER_FILE, orders)

                    write_log(
                        f"Order Cancelled | "
                        f"Customer: {self.customer_name} | "
                        f"Order ID: {self.order_id}"
                    )

                    print("✅ Order Cancelled Successfully!")
                    return

            print("❌ Invalid Order ID. This order does not belong to you.")

        except Exception:
            logging.exception(
                f"Unexpected error while cancelling order | "
                f"User: {self.customer_name}"
            )

            print("❌ Something went wrong!")


