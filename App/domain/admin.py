from app.domain.user import User
# from app.food_management.view_food import ViewFoodManager
# from app.food_management.add_food import AddFoodManager
# from app.food_management.update_food import UpdateFoodManager
# from app.food_management.dalate_food import DeleteFoodManager
# from app.services.view_all_orders import ViewAllOrdersServices
# from app.services.update_order_status import UpdateOrderStatusServices
from app.menu.food_menu_management import menu_management
from app.menu.order_management import order_management
from app.menu.staff_management import staff_management
from app.menu.reports_menu import reports

class Admin(User):

    # def view_food_menu(self):
    #     ViewFoodManager().view_food_menu()

    # def add_food(self):
    #     AddFoodManager().add_food()

    # def update_food(self):
    #     UpdateFoodManager().update_food()

    # def delete_food(self):
    #     DeleteFoodManager().delete_food()

    def menu_management(self):
        menu_management()

    def order_management(self):
        order_management()

    def staff_management(self):
        staff_management()

    def reports_menu(self):
        reports()

    # def view_all_orders(self):
    #     ViewAllOrdersServices().view_all_orders()
    
    # def update_order_status(self):
    #     UpdateOrderStatusServices().update_order_status()

    # def view_staff(self):
    #     print("Displaying staff members.")
    
    # def add_staff(self):
    #     print("Staff member added successfully.")
    
    # def remove_staff(self):
    #     print("Staff member removed successfully.")
    