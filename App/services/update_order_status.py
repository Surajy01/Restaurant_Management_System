from App.utils.file_handler import read_data, write_data

ORDER_FILE="App/database/orders.json"

class UpdateOrderStatusServices:

    def update_order_status(self):

        orders=read_data(ORDER_FILE)

        if not orders:
            print("No Orders Found!")
            return

        print("\n===== ORDER LIST =====")

        for index, order in enumerate(orders, start=1):

            print(
                f"{index}. "
                f"Order ID: {order['order_id']} | "
                f"Customer: {order['customer_name']} | "
                f"Status: {order['status']}"
            )

        try:
            choice=int(input("\nSelect Order Number: "))
            order=orders[choice - 1]

        except (ValueError, IndexError):
            print("Invalid Choice!")
            return

        print("\n===== UPDATE ORDER STATUS =====")
        print("1. Preparing")
        print("2. Ready")
        print("3. Delivered")
        print("4. Cancelled")

        status_choice=input("Select Status: ")

        status_map={
            "1": "Preparing",
            "2": "Ready",
            "3": "Delivered",
            "4": "Cancelled"
        }

        new_status=status_map.get(status_choice)

        if not new_status:
            print("Invalid Status!")
            return

        order["status"]=new_status

        write_data(ORDER_FILE, orders)

        print("\nOrder Status Updated Successfully!")
        print(f"Order ID : {order['order_id']}")
        print(f"Customer : {order['customer_name']}")
        print(f"Status   : {new_status}")
        
    

