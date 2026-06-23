from app.utils.file_handler import read_data, write_data

ORDER_FILE = "app/database/orders.json"

class ViewAllOrdersServices:
    
    # def __init__(self):
    #     pass


    def view_all_orders(self):

        orders=read_data(ORDER_FILE)

        if not orders:
            print("\n❌ No Orders Found!")
            return

        print("\n" + "═" * 65)
        print("📋 ALL ORDERS REPORT 📋".center(65))
        print("═" * 65)

        for order in orders:

            print("\n┌" + "─" * 39 + "┐")
            print(f"│ 🆔 Order ID       : {order['order_id']:<18}│")
            print(f"│ 👤 Customer       : {order['customer_name']:<18}│")
            print(f"│ 📞 Phone          : {order.get('customer_phone', 'N/A'):<18}│")
            print(f"│ 🛒 Ordered By     : {order.get('ordered_by', 'Customer'):<18}│")

            if order.get("staff_name"):
                print(f"│ 👨‍🍳 Staff Name     : {order['staff_name']:<16}│")

            print(f"│ 📦 Order Status   : {order['status']:<18}│")
            print(f"│ 💳 Payment Status : {order['payment_status']:<18}│")
            print(f"│ 💰 Final Amount   : ₹{str(order['final_total']):<17}│")
            print("└" + "─" * 39 + "┘")

            print("\n🍽  ORDER ITEMS")
            print("┌────┬──────────────────────┬───────┬──────────┬──────────┐")
            print("│ No │ Food Name            │ Qty   │ Price    │ Total    │")
            print("├────┼──────────────────────┼───────┼──────────┼──────────┤")

            for index, item in enumerate(order["items"], start=1):

                print(
                    f"│ {index:<2} "
                    f"│ {item['food_name'][:20]:<20} "
                    f"│ {item['quantity']:<5} "
                    f"│ ₹{item['price']:<7} "
                    f"│ ₹{item['total']:<7} │"
                )

            print("└────┴──────────────────────┴───────┴──────────┴──────────┘")

            print(f"🧾 Grand Total : ₹{order['final_total']}")
            print("")
            print("*" * 65)

    
    # def update_order_status(self, order_id, new_status):

    #     orders=read_data(ORDER_FILE)

    #     for order in orders:
    #         if order['order_id']==order_id:
    #             order['status']=new_status
    #             write_data(ORDER_FILE, orders)
    #             print(f"Order ID: {order_id} has been updated to status: {new_status}")
    #             return
        
    #     print(f"Order ID: {order_id} not found.")


    