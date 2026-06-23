from app.utils.file_handler import read_data, write_data

ORDER_FILE="app/database/orders.json"

# class CancelOrder:
#     def __init__(self, order_id):
#         self.order_id=order_id

#     def execute(self):
#         orders=read_data(ORDER_FILE)

#         for order in orders:
#             if order['order_id']==self.order_id:
#                 if order['status'] in ['Delivered', 'Cancelled']:
#                     print(f"Order ID {self.order_id} cannot be cancelled as it is already {order['status']}.")
#                     return
#                 else:
#                     order['status']='Cancelled'
#                     write_data(ORDER_FILE, orders)
#                     print(f"Order ID {self.order_id} has been cancelled successfully.")
#                     return

#         print(f"Order ID {self.order_id} not found.")

class CancelOrder:

    def __init__(self, customer_name, order_id):
        self.customer_name=customer_name
        self.order_id=order_id

    def execute(self):

        orders=read_data(ORDER_FILE)

        customer_orders=[
            order for order in orders
            if order["customer_name"]==self.customer_name
        ]

        if not customer_orders:
            print("You have no orders.")
            return

        for order in customer_orders:

            if order["order_id"]==self.order_id:

                if order["status"] in ["Delivered", "Cancelled"]:

                    print(
                        f"Order ID {self.order_id} cannot be cancelled "
                        f"because it is already {order['status']}."
                    )
                    return

                order["status"]="Cancelled"

                write_data(ORDER_FILE, orders)

                print(
                    f"Order ID {self.order_id} has been "
                    f"cancelled successfully."
                )
                return

        print("Invalid Order ID. This order does not belong to you.")




