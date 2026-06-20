from App.domain.user import User
from App.food_management.view_food import ViewFoodManager
from App.order.order_place import OrderService
from App.order.cancel_order import CancelOrder
from App.menu.payment_menu import payment_menu
from App.menu.table_menu import table_menu

class Customer(User):

    def view_food_menu(self):
        ViewFoodManager().view_food_menu()
    
    def place_order(self):
        OrderService().order_food(self.username)
    
    def view_orders(self):
        OrderService().view_orders(self.username)

    def cancel_order(self):
       self.order_id=input("Order ID: ")
       CancelOrder(customer_name=self.username, order_id=self.order_id).execute()

    def Generate_bill(self):
        print("Displaying your bill.")

    def Pay_bill(self,order_id):
        payment_menu(order_id)
    
    def table_booking(self):
        table_menu(self.username)        
    