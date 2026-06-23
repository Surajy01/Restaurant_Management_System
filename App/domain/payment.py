import uuid
from app.services.payment_services import PaymentService
# from app.services.update_order_status import UpdateOrderStatusServices

class Payment:
        def __init__(self,user_name,order_id, amount):
            self.user_name=user_name
            self.order_id=order_id
            self.amount=amount
        
class CashPayment(Payment):
    
    def process_payment(self):

        payment_service = PaymentService()

        payment_service.save_payment(
            self.order_id,
            self.user_name,
            self.amount,
            "Cash"
        )
        payment_service.update_payment_status(self.order_id)

        print(f"Cash Payment Successful!")
        print(f"Name: {self.user_name}")
        print(f"Amount Paid: ₹{self.amount}")

class UPIPayment(Payment):

    def process_payment(self):

        upi_id = input("Enter UPI ID: ").strip()

        if "@" not in upi_id or len(upi_id) < 5:
            print("❌ Invalid UPI ID format!")
            return

        print("\nSelect UPI App:")
        print("1. Google Pay")
        print("2. PhonePe")
        print("3. Paytm")

        apps = {
            "1": "Google Pay",
            "2": "PhonePe",
            "3": "Paytm"
        }

        app_choice = input("Choose App: ")
        upi_app = apps.get(app_choice, "Other")

        txn_id = str(uuid.uuid4())[:10]

        payment_service = PaymentService()

        # Update order status first
        payment_service.update_payment_status(self.order_id)

        # Save payment record
        payment_service.save_payment(
            self.order_id,
            self.user_name,
            self.amount,
            "UPI"
        )

        print("\n✅ UPI Payment Successful!")
        print(f"👤 Name        : {self.user_name}")
        print(f"📱 UPI ID      : {upi_id}")
        print(f"🏦 UPI App     : {upi_app}")
        print(f"💳 Transaction : {txn_id}")
        print(f"💰 Amount Paid : ₹{self.amount}")


class CardPayment(Payment):

    def process_payment(self):

        print("\n" + "═" * 60)
        print("💳 CARD PAYMENT GATEWAY 💳".center(60))
        print("═" * 60)

        card_no = input("🔢 Enter Card Number: ").strip()

        if not card_no.isdigit() or len(card_no) != 16:
            print("❌ Invalid Card Number!")
            return

        expiry = input("📅 Enter Expiry Date (MM/YY): ").strip()
        cvv = input("🔒 Enter CVV: ").strip()

        if len(cvv) != 3 or not cvv.isdigit():
            print("❌ Invalid CVV!")
            return

        print("\nProcessing Payment...\n")

        txn_id = str(uuid.uuid4())[:10]

        payment_service = PaymentService()

        payment_service.save_payment(
            self.order_id,
            self.user_name,
            self.amount,
            "Card"
        )

        payment_service.update_payment_status(self.order_id)

        print("\n" + "✔ PAYMENT SUCCESSFUL ✔".center(60))
        print("═" * 60)
        print(f"👤 Name              : {self.user_name}")
        print(f"💰 Amount Paid       : ₹{self.amount}")
        print(f"💳 Card Ending       : **** **** **** {card_no[-4:]}")
        print(f"📅 Expiry            : {expiry}")
        print(f"🧾 Transaction ID    : {txn_id}")
        print("═" * 60)
        print("🙏 Thank you for dining with us!".center(60))
        print("═" * 60)



        