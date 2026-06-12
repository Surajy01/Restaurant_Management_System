from App.domain.user import User
from App.food_management.view_food import ViewFoodManager
from App.food_management.add_food import AddFoodManager
from App.food_management.update_food import UpdateFoodManager
from App.food_management.dalate_food import DeleteFoodManager

class Admin(User):

    def view_food_menu(self):
        ViewFoodManager().view_food_menu()

    def add_food(self):
        AddFoodManager().add_food()

    def update_food(self):
        UpdateFoodManager().update_food()

    def delete_food(self):
        DeleteFoodManager().delete_food()

    def view_all_orders(self):
        print("Displaying all orders.")
    
    def update_order_status(self):
        print("Order status updated successfully.")

    def view_staff(self):
        print("Displaying staff members.")
    
    def add_staff(self):
        print("Staff member added successfully.")
    
    def remove_staff(self):
        print("Staff member removed successfully.")
    