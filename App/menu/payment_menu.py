from app.domain.payment import CashPayment,UPIPayment,CardPayment
from app.services.payment_services import PaymentService

def payment_menu(order_id):

    payment_service=PaymentService()
    order=payment_service.get_order_by_id(order_id)

    if not order:
        print("Order not found!")
        return

    user_name=order["customer_name"]
    amount=order["final_total"]

    while True:

        print("\n" + "═" * 60)
        print("💳  BILL PAYMENT GATEWAY  💳".center(60))
        print("═" * 60)

        print(f"🧾 Order ID  : {order_id}")
        print(f"👤 Customer  : {user_name}")
        print(f"💰 Amount    : ₹{amount}")

        print("─" * 60)

        print("1️⃣  Cash Payment")
        print("2️⃣  UPI Payment (PhonePe / GPay / Paytm)")
        print("3️⃣  Card Payment (Debit / Credit)")
        print("4️⃣  🔙 Back ")

        print("─" * 60)

        choice = input("👉 Enter your choice: ")

        if choice=="1":
            CashPayment(user_name,order_id,amount).process_payment()
            break

        elif choice=="2":
           UPIPayment(user_name,order_id,amount).process_payment()
           break

        elif choice=="3":
            CardPayment(user_name,order_id,amount).process_payment()
            break

        elif choice=="4":
            print("Exiting...")
            break