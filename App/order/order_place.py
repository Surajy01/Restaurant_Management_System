import uuid
from App.utils.file_handler import read_data, write_data

FOOD_FILE="App/database/foods.json"
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

            print("\n===== FOOD MENU =====")

            for index, food in enumerate(foods, start=1):

                status=("Available" if food["stock"] > 0 else "Not Available")

                print(
                    f"{index}. {food['name']} "
                    f"({food['category']}) - "
                    f"{food['unit']} - "
                    f"₹{food['price']} "
                    f"[{status}]"
                )

            try:
                choice=int(input("\nSelect Food Number: "))
                food=foods[choice - 1]

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
            "status": "Pending"
        }

        orders.append(order)

        write_data(ORDER_FILE, orders)

        print("\n===== ORDER SUCCESSFUL =====")
        print(f"Order ID : {order['order_id']}")
        print(f"Customer : {customer_name}")

        print("\nItems Ordered:")
        print()

        for item in cart:

            print(
                f"{item['food_name']} | "
                f"{item['quantity']} {item['unit']} | "
                f"₹{item['price']} each | "
                f"₹{item['total']}"
            )

        print("-" * 50)
        print(f"Grand Total : ₹{grand_total}")
        print(f"Status      : {order['status']}")


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

