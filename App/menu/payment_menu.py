# from App.payment.cash_payment import CashPayment
# from App.payment.upi_payment import UPIPayment
# from App.payment.card_payment import CardPayment

from App.domain.payment import CashPayment,UPIPayment,CardPayment
from App.services.payment_services import PaymentService

def payment_menu(order_id):

    payment_service=PaymentService()
    order=payment_service.get_order_by_id(order_id)

    if not order:
        print("Order not found!")
        return

    user_name=order["customer_name"]
    amount=order["grand_total"]

    while True:
        print("\n===== BILL PAYMENT =====")
        print(f"Order ID : {order_id}")
        print(f"Customer : {user_name}")
        print(f"Amount   : ₹{amount}")

        print("1. Cash Payment")
        print("2. UPI Payment")
        print("3. Debit/Credit Card Payment")
        print("4. Back to Main Menu")
        print("5. Exit")

        choice=input("Enter choice: ")

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
            print("Back to Main Menu")
            break
        elif choice=="5":
            print("Exiting...")
            break