import uuid
from App.utils.file_handler import read_data, write_data
from datetime import datetime

FOOD_FILE="App/database/food.json"
ORDER_FILE="App/database/orders.json"


class OrderService:

    def order_food(self, customer_name):

        foods=read_data(FOOD_FILE)

        if not foods:
            print("No food items available!")
            return

        cart=[]
        grand_total=0

        while True:

            print("\n" + "═" * 70)
            print("🍽 FOOD MENU 🍽".center(70))
            print("═" * 70)

            print("╔════╦══════════════════╦════════════╦═════════╦══════════╦═══════╗")
            print("║ No ║ Food Name        ║ Category   ║ Unit    ║ Price    ║ Stock ║")
            print("╠════╬══════════════════╬════════════╬═════════╬══════════╬═══════╣")

            for index, food in enumerate(foods, start=1):

                status="✓" if food["stock"] > 0 else "✗"

                print(
                    f"║ {index:<2} "
                    f"║ {food['name'][:16]:<16} "
                    f"║ {food['category'][:10]:<10} "
                    f"║ {food['unit'][:7]:<7} "
                    f"║ ₹{food['price']:<7} "
                    f"║ {status:^5} ║"
                )

            print("╚════╩══════════════════╩════════════╩═════════╩══════════╩═══════╝")

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

        # Create order
        order={
            "order_id": str(uuid.uuid4())[:8],
            "customer_name": customer_name,
            "items": cart,
            "grand_total": grand_total,
            "status": "Pending",
            "payment_status":"Unpaid"
        }

        orders.append(order)

        write_data(ORDER_FILE, orders)
        invoice_date=datetime.now().strftime("%d-%m-%Y %I:%M %p")
        gst_rate=5  # 5%
        gst_amount=(grand_total * gst_rate) / 100
        final_total=grand_total + gst_amount

        print("\n" + "=" * 80)
        print("🧾 SURAJ RESTAURANT INVOICE 🧾".center(80))
        print("=" * 80)

        print(f"Order ID        : {order['order_id']}")
        print(f"Customer Name   : {customer_name}")
        # print(f"Phone Number    : {phone}")
        print(f"Phone Number    : 1234567890")
        print(f"Date & Time     : {invoice_date}")
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



        # print("\n===== ORDER SUCCESSFUL =====")
        # print(f"Order ID : {order['order_id']}")
        # print(f"Customer : {customer_name}")

        # print("\nItems Ordered:")
        # print()

        # for item in cart:

        #     print(
        #         f"{item['food_name']} | "
        #         f"{item['quantity']} {item['unit']} | "
        #         f"₹{item['price']} each | "
        #         f"₹{item['total']}"
        #     )

        # print("-" * 50)
        # print(f"Grand Total : ₹{grand_total}")
        # print(f"Status      : {order['status']}")
        # print(f"Payment Status : {order['payment_status']}")


    def view_orders(self, customer_name):

        orders=read_data(ORDER_FILE)

        customer_orders=[order for order in orders if order["customer_name"]==customer_name]

        if not customer_orders:
            print("You have no orders yet!")
            return

        print("\n" + "=" * 60)
        print("                 YOUR ORDER DETAILS")
        print("=" * 60)

        for order in customer_orders:

            print(f"\nOrder ID      : {order['order_id']}")
            print(f"Customer Name : {order['customer_name']}")
            print(f"Order Status  : {order['status']}")
            print(f"Payment Status : {order['payment_status']}")

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

