from App.domain.user import User
from App.food_management.view_food import ViewFoodManager
from App.order.order_place import OrderService


class Customer(User):

    def view_food_menu(self):
        ViewFoodManager().view_food_menu()
    
    def place_order(self):
        OrderService().order_food(self.username)
        # print("Order placed successfully.")
    
    def view_orders(self):
        OrderService().view_orders(self.username)
        # print("Displaying your orders.")

    def cancel_order(self):
        print("Order cancelled successfully.")
    
    def view_bill(self):
        print("Displaying your bill.")
    
    def table_booking(self):
        print("Table booked successfully.")
    