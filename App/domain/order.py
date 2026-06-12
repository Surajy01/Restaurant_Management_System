class Order:
    def __init__(self, order_id, customer_id,customer_name,
        food_name, quantity, price, total_price, status="Pending"):
        self.order_id=order_id
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.food_name=food_name
        self.quantity=quantity
        self.price=price
        self.total_price=total_price
        self.status=status
    
    def dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "food_name": self.food_name,
            "quantity": self.quantity,
            "price": self.price,
            "total_price": self.total_price,
            "status": self.status
        }


        