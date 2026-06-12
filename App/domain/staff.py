
from App.domain.user import User
from App.food_management.view_food import ViewFoodManager

class Staff(User):

    def view_food_menu(self):
        ViewFoodManager().view_food_menu()

    def view_orders(self):
        print("Displaying all orders.")
    
    def update_order_status(self):
        print("Order status updated successfully.")
    
    def manage_menu(self):
        print("Menu managed successfully.")
    
    def view_sales_report(self):
        print("Displaying sales report.")