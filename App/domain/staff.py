from app.domain.user import User
from app.food_management.view_food import ViewFoodManager
from app.menu.payment_menu import payment_menu
from app.order.order_place import OrderService
from app.menu.table_menu import table_menu
from app.menu.order_management import order_management
from app.order.cancel_order import CancelOrder

class Staff(User):
    def __init__(self,user_id,username,email,phone,password,dob,address,role,department,experience,salary=0):
        super().__init__(user_id,username,email,phone,password,dob,address,role,department,experience)
        self.salary=salary

    def dict(self):
        data=super().dict()
        data["salary"]=self.salary
        return data
    
    def view_food_menu(self):
        ViewFoodManager().view_food_menu()

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

    def payment_menus(self,order_id):
        payment_menu(order_id)

    def table_reservation(self):
        table_menu(self.username)

    def order_management(self):
        order_management(self)

    def cancel_order(self):
       self.order_id=input("Order ID: ")
       CancelOrder(customer_name=self.username, order_id=self.order_id,role=self.role).execute()

