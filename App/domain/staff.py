from app.domain.user import User
from app.food_management.view_food import ViewFoodManager
# from app.services.update_order_status import UpdateOrderStatusServices
# from app.services.view_all_orders import ViewAllOrdersServices
from app.menu.payment_menu import payment_menu
from app.order.order_place import OrderService
from app.menu.table_menu import table_menu
from app.menu.order_management import order_management

class Staff(User):

    def view_food_menu(self):
        ViewFoodManager().view_food_menu()

    # def view_orders(self):
    #     ViewAllOrdersServices().view_all_orders()
    
    # def update_order_status(self):
    #     UpdateOrderStatusServices().update_order_status()

    def take_order(self):
        customer_name=input("Enter Customer Name: ")
        customer_phone=input("Enter Customer Phone: ")
        if not customer_phone.isdigit() or len(customer_phone) != 10:
            print("❌ Phone Number must be exactly 10 digits!")
            return
        OrderService().order_food(customer_name=customer_name,
        customer_phone=customer_phone,
        ordered_by="Staff",
        staff_name=self.username)

    # def manage_menu(self):
    #     print("Menu managed successfully.")
    
    # def view_sales_report(self):
    #     print("Displaying sales report.")

    # def view_available_foods(self):
    #     print("View All Foods")

    def payment_menus(self,order_id):
        payment_menu(order_id)

    def table_reservation(self):
        table_menu(self.username)

    def order_management(self):
        order_management()
