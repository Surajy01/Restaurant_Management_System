from App.services.payment_services import PaymentService
# from App.services.update_order_status import UpdateOrderStatusServices

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
        upi_id = input("Enter UPI ID: ")

        payment_service=PaymentService()

        payment_service.save_payment(
            self.order_id,
            self.user_name,
            self.amount,
            "UPI"

        )

        payment_service.update_payment_status(self.order_id)

        print(f"UPI Payment Successful!")
        print(f"Name: {self.user_name}")
        print(f"UPI ID: {upi_id}")
        print(f"Amount Paid: ₹{self.amount}")

class CardPayment(Payment):

    # def __init__(self, amount):
    #     super().__init__(amount)

    def process_payment(self):

        card_no = input("Enter Card Number: ")

        payment_service=PaymentService()
        payment_service.save_payment(
            self.order_id,
            self.user_name,
            self.amount,
            "Card"
        )
        payment_service.update_payment_status(self.order_id)

        print(f"Card Payment Successful!")
        print(f"Name: {self.user_name}")
        print(f"Amount Paid: ₹{self.amount}")
        print(f"Card Ending With: {card_no[-4:]}")
