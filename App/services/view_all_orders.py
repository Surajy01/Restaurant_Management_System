from App.utils.file_handler import read_data, write_data

ORDER_FILE = "App/database/orders.json"

class ViewAllOrdersServices:
    
    # def __init__(self):
    #     pass

    # def admin_login(self, username, password):
    #     if username == "admin" and password == "admin123":
    #         return True
    #     else:
    #         return False
    
    def view_all_orders(self):

        orders=read_data(ORDER_FILE)

        if not orders:
            print("No Orders Found!")
            return

        print("\n" + "=" * 60)
        print("                 ALL ORDER DETAILS")
        print("=" * 60)

        for order in orders:

            print(f"\nOrder ID    : {order['order_id']}")
            print(f"Customer Name : {order['customer_name']}")
            print(f"Order Status  : {order['status']}")

            print("-" * 60)
            print(
                f"{'Food Item':<20}"
                f"{'Qty':<8}"
                f"{'Unit':<15}"
                f"{'Price':<10}"
                f"{'Total'}"
            )
            print("-" * 60)

            for item in order["items"]:

                print(
                    f"{item['food_name']:<20}"
                    f"{item['quantity']:<8}"
                    f"{item['unit']:<15}"
                    f"₹{item['price']:<9}"
                    f"₹{item['total']}"
                )

            print("-" * 60)
            print(f"{'Grand Total':<52} ₹{order['grand_total']}")
            print("=" * 60)
    
    # def update_order_status(self, order_id, new_status):

    #     orders=read_data(ORDER_FILE)

    #     for order in orders:
    #         if order['order_id']==order_id:
    #             order['status']=new_status
    #             write_data(ORDER_FILE, orders)
    #             print(f"Order ID: {order_id} has been updated to status: {new_status}")
    #             return
        
    #     print(f"Order ID: {order_id} not found.")


    