import uuid
from app.utils.file_handler import read_data, write_data
from datetime import datetime
from app.menu.payment_menu import payment_menu
from app.utils.logger import write_log
import logging

FOOD_FILE="app/database/food.json"
ORDER_FILE="app/database/orders.json"
# USER_FILE="app/database/sign_up.json"


class OrderService:

    def order_food(self, customer_name, customer_phone, ordered_by, staff_name=None):

        try:

            foods=read_data(FOOD_FILE)

            if not foods:
                logging.error("Order Placement Failed | No food items available in menu")
                print("No food items available!")
                return
            
            # Sort foods by category
            category_order={
                "Breakfast": 1,
                "Starters": 2,
                "Main Course": 3,
                "Beverages": 4,
                "Desserts": 5
            }

            foods.sort(
                key=lambda food: category_order.get(
                    food["category"],
                    999
                )
            )

            cart=[]
            grand_total=0

            while True:

                print("\n" + "═" * 90)
                print("🍽 FOOD MENU 🍽".center(90))
                print("═" * 90)

                print("╔════╦══════════════════╦══════════════╦═════════╦═════════╦══════════╦═══════╗")
                print("║ No ║ Food Name        ║ Category     ║ Type    ║ Unit    ║ Price    ║ Stock ║")
                print("╠════╬══════════════════╬══════════════╬═════════╬═════════╬══════════╬═══════╣")

                for index, food in enumerate(foods, start=1):

                    status = "✓" if food["stock"] > 0 else "✗"

                    food_type = food.get("food_type", "Veg")

                    print(
                        f"║ {index:<2} "
                        f"║ {food['name'][:16]:<16} "
                        f"║ {food['category'][:12]:<12} "
                        f"║ {food_type[:7]:<7} "
                        f"║ {food['unit'][:7]:<7} "
                        f"║ ₹{food['price']:<7} "
                        f"║ {status:^5} ║"
                    )

                print("╚════╩══════════════════╩══════════════╩═════════╩═════════╩══════════╩═══════╝")
                # try:
                    # choice=int(input("\nSelect Food Number: "))
                    # food=foods[choice - 1]

                try:

                    user_input=input("\nSelect Food Number or Enter Food Name: ").strip()

                    # Select by number
                    if user_input.isdigit():

                        choice=int(user_input)
                        food=foods[choice - 1]

                    # Search by food name
                    else:

                        search=user_input.lower()

                        matched_foods=[
                            item for item in foods
                            if search in item["name"].lower()
                        ]

                        if not matched_foods:
                            print("Food not found!")
                            continue

                        if len(matched_foods)==1:
                            food=matched_foods[0]

                        else:
                            print("\n===== MATCHING FOODS =====")

                            for index, item in enumerate(matched_foods, start=1):
                                print(
                                    f"{index}. {item['name']} "
                                    f"({item['category']}) - ₹{item['price']}"
                                )

                            sub_choice=int(input("Select Food: "))
                            food=matched_foods[sub_choice - 1]

                except (ValueError, IndexError):

                    logging.error(f"Invalid Food Selection | Customer: {customer_name}")
                    print("Invalid Choice!")
                    continue
                    

                if food["stock"]<=0:
                    print(f"{food['name']} is currently not available!")
                    continue

                try:
                    qty=int(input("Enter Quantity: "))

                except ValueError:
                    print("Quantity must be a number!")
                    continue

                if qty<=0:
                    print("Quantity must be greater than 0!")
                    continue

                if qty>food["stock"]:
                    logging.error(
                        f"Insufficient Stock | "
                        f"Food: {food['name']} | "
                        f"Requested: {qty} | "
                        f"Available: {food['stock']}"
                    )

                    print(f"Only {food['stock']} {food['unit']} available!")
                    continue

                item_total=qty * food["price"]

                cart.append({
                    "food_name": food["name"],
                    "category": food["category"],
                    "unit": food["unit"],
                    "quantity": qty,
                    "price": food["price"],
                    "total": item_total
                })

                # Update stock immediately
                food["stock"] -= qty

                grand_total += item_total

                print(f"{food['name']} added to cart successfully!")

                more=input("\nDo you want to add more items? (y/n): ").lower()

                if more != "y":
                    break

            if not cart:
                print("No items selected!")
                return

            # Save updated stock
            write_data(FOOD_FILE, foods)

            # Read existing orders
            orders=read_data(ORDER_FILE)

            invoice_date=datetime.now().strftime("%d-%m-%Y")
            invoice_time=datetime.now().strftime("%I:%M %p")
            gst_rate=5  # 5%
            gst_amount=(grand_total * gst_rate) / 100
            final_total=grand_total + gst_amount
            # Create order
            order={
                "order_id": str(uuid.uuid4())[:8],
                "customer_name": customer_name,
                "customer_phone": customer_phone,
                "ordered_by": ordered_by,
                "order_date": datetime.now().strftime("%d-%m-%Y"),
                "order_time": datetime.now().strftime("%I:%M %p"),
                "staff_name": staff_name,
                "items": cart,
                "grand_total": grand_total,
                "final_total": final_total,
                "status": "Pending",
                "payment_status":"Unpaid"
            }

            orders.append(order)

            write_data(ORDER_FILE, orders)

            write_log(
                f"Order Placed Successfully | "
                f"Order ID: {order['order_id']} | "
                f"Customer: {customer_name} | "
                f"Phone: {customer_phone} | "
                f"Final Amount: Rs.{final_total} | "
                f"Ordered By: {ordered_by}"
            )

            # users=read_data(USER_FILE)

            # for user in users:
            #     if user["username"]==customer_name:
            #         customer_phone=user["phone"]
            #         break 

            print("\n" + "=" * 80)
            print("🧾 SURAJ RESTAURANT INVOICE 🧾".center(80))
            print("=" * 80)

            print(f"Order ID        : {order['order_id']}")
            print(f"Customer Name   : {customer_name}")
            print(f"Phone Number    : {customer_phone}")

            if ordered_by == "Staff":
                print(f"Ordered By      : {ordered_by}")

            if ordered_by == "Staff":
                print(f"Staff Name      : {staff_name}")

            print(f"Date     : {invoice_date}")
            print(f"Time     : {invoice_time}")
            print(f"Order Status    : {order['status']}")
            print(f"Payment Status  : {order['payment_status']}")

            print("-" * 80)

            print(
                f"{'Item':<25}"
                f"{'Qty':<15}"
                f"{'Unit Price':<15}"
                f"{'Total':<15}"
            )

            print("-" * 80)

            for item in cart:

                print(
                    f"{item['food_name']:<25}"
                    f"{str(item['quantity']) + ' ' + item['unit']:<15}"
                    f"₹{item['price']:<14.2f}"
                    f"₹{item['total']:<14.2f}"
                )

            print("-" * 80)

            print(f"{'Subtotal':<60} ₹{grand_total:.2f}")
            print(f"{'GST (' + str(gst_rate) + '%)':<60} ₹{gst_amount:.2f}")
            print(f"{'Final Amount':<60} ₹{final_total:.2f}")

            print("=" * 80)
            print("🙏 Thank You For Visiting Suraj Restaurant 🙏".center(80))
            print("=" * 80)

            if ordered_by=="Customer":

                pay_now=input("\nDo you want to pay the bill now? (y/n): ").lower()

                # if pay_now == "y":
                #     PaymentService().pay_bill(
                #         order["order_id"],
                #         final_total
                #     )

                if pay_now == "y":
                    write_log(
                        f"Customer Selected Immediate Payment | "
                        f"Order ID: {order['order_id']} | "
                        f"Customer: {customer_name}"
                    )
                    payment_menu(order["order_id"])
                else:
                    write_log(
                        f"Payment Pending | "
                        f"Order ID: {order['order_id']} | "
                        f"Customer: {customer_name}"
                    )
                    print("💳 Payment Pending!")

        except Exception:
            logging.exception(
                f"Unexpected Error While Placing Order | "
                f"Customer: {customer_name}"
            )

            print("❌ Something went wrong while placing the order!")

    def view_orders_history(self, customer_name):

        try:
            write_log(f"Viewed Order History | "
                f"Customer: {customer_name}"
            )
            orders=read_data(ORDER_FILE)

            customer_orders=[order for order in orders if order["customer_name"]==customer_name]

            if not customer_orders:
                logging.error(
                    f"No Order History Found | Customer: {customer_name}"
                )
                print("You have no orders yet!")
                return

            print("\n" + "═" * 60)
            print("🧾 MY ORDER HISTORY 🧾".center(60))
            print("═" * 60)

            for order in customer_orders:

                print("\n╔" + "═" * 50 + "╗")
                print("║              📋 ORDER DETAILS                    ║".center(50))
                print("╠" + "═" * 50 + "╣")

                print(f"║ 🆔 Order ID       : {order['order_id']:<29}║")
                print(f"║ 👤 Name           : {order['customer_name']:<29}║")
                print(f"║ 📦 Order Status   : {order['status']:<29}║")
                print(f"║ 💳 Payment Status : {order['payment_status']:<29}║")

                if "payment_method" in order:
                    print(f"║ 💰 Payment Method : {order['payment_method']:<29}║")

                if "order_date" in order:
                    print(f"║ 📅 Order Date     : {order['order_date']:<29}║")

                if "order_time" in order:
                    print(f"║ 📅 Order Time     : {order['order_time']:<29}║")

                print("╚" + "═" * 50 + "╝")

                print("\n🍽 ORDER ITEMS")
                print("┌────┬──────────────────────┬────────┬──────────┬──────────┐")
                print("│ No │ Food Name            │ Qty    │ Price    │ Total    │")
                print("├────┼──────────────────────┼────────┼──────────┼──────────┤")

                for index, item in enumerate(order["items"], start=1):

                    print(
                        f"│ {index:<2} "
                        f"│ {item['food_name'][:20]:<20} "
                        f"│ {item['quantity']:<6} "
                        f"│ ₹{item['price']:<7} "
                        f"│ ₹{item['total']:<7} │"
                    )

                print("└────┴──────────────────────┴────────┴──────────┴──────────┘")

                print(f"\n🧾 Grand Total : ₹{order['final_total']}")
                print("")
                print("*" * 60)
        except Exception:

            logging.exception(
                f"Unexpected Error While Viewing Orders | "
                f"Customer: {customer_name}"
            )

            print("❌ Something went wrong!")
