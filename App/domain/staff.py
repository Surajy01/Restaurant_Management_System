from App.domain.user import User
from App.food_management.view_food import ViewFoodManager
from App.services.update_order_status import UpdateOrderStatusServices
from App.services.view_all_orders import ViewAllOrdersServices
from App.menu.payment_menu import payment_menu
from App.order.order_place import OrderService
class Staff(User):

    def view_food_menu(self):
        ViewFoodManager().view_food_menu()

    def view_orders(self):
        ViewAllOrdersServices().view_all_orders()
        # print("Displaying all orders.")
    
    def update_order_status(self):
        UpdateOrderStatusServices().update_order_status()
        # print("Order status updated successfully.")
    def take_order(self):
        OrderService().order_food(self.username)

    def manage_menu(self):
        print("Menu managed successfully.")
    
    def view_sales_report(self):
        print("Displaying sales report.")

    def payment_menus(self,order_id):
        payment_menu(order_id)