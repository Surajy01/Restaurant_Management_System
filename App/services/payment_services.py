from App.utils.file_handler import read_data,write_data

PAYMENT_FILE="App/database/payments.json"
ORDER_FILE="App/database/orders.json"

class PaymentService:
    # def __init__(self, amount):
    #     self.amount = amount

    # def process_payment(self, payment_method):
    #     payment_method.process_payment()

    def get_order_by_id(self,order_id):

        orders=read_data(ORDER_FILE)

        for order in orders:
            if order["order_id"]==order_id:
                return order
        return None
    
    def update_payment_status(self, order_id):
        orders = read_data(ORDER_FILE)

        for order in orders:
            if order["order_id"] == order_id:
                order["payment_status"] = "Paid"
                break

        write_data(ORDER_FILE, orders)
        
    def save_payment(self,order_id,user_name,amount,payment_method):

        payments=read_data(PAYMENT_FILE)

        payment_details={
            "order_id": order_id,
            "user_name": user_name,
            "amount": amount,
            "payment_method": payment_method
        }
        payments.append(payment_details)
        
        write_data(PAYMENT_FILE,payments)
