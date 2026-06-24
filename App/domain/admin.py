from app.domain.user import User
from app.menu.food_menu_management import menu_management
from app.menu.order_management import order_management
from app.menu.staff_management import staff_management
from app.menu.reports_menu import reports
from app.order.cancel_order import CancelOrder


class Admin(User):

    def menu_management(self):
        menu_management()

    def order_management(self):
        order_management(self)

    def staff_management(self):
        staff_management()

    def reports_menu(self):
        reports()

    def cancel_order(self):
       self.order_id=input("Order ID: ")
       CancelOrder(customer_name=self.username, order_id=self.order_id,role=self.role).execute()


    