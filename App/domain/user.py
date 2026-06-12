class User:
    def __init__(self,user_id,username,email,phone,password,dob,address,role,department=None,experience=None):
        self.user_id=user_id
        self.username=username
        self.email=email
        self.phone=phone
        self.password=password
        self.dob=dob
        self.address=address
        self.role=role
        self.department=department
        self.experience=experience

    # it is used to convert the user object into a dictionary format for easy storage.
    def dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "dob": self.dob,
            "address": self.address,
            "role": self.role,
            "department": self.department,
            "experience": self.experience
        }

#     def display_profile(self):
#         print("\n===== USER PROFILE =====")
#         print(f"ID      : {self.user_id}")
#         print(f"Name    : {self.username}")
#         print(f"Email   : {self.email}")
#         print(f"Phone   : {self.phone}")
#         print(f"DOB     : {self.dob}")
#         print(f"Address : {self.address}")
#         print(f"Role    : {self.role}")
#         print(f"Department : {self.department}")
#         print(f"Experience : {self.experience}")


# class Admin(User):

#     def add_food(self):
#         print("Food item added successfully.")

#     def update_food(self):
#         print("Food item updated successfully.")

#     def delete_food(self):
#         print("Food item deleted successfully.")

#     def view_orders(self):
#         print("Displaying all orders.")

#     def manage_staff(self):
#         print("Managing staff.")


# class Staff(User):

#     def view_menu(self):
#         print("Displaying food menu.")

#     def take_order(self):
#         print("Order placed successfully.")

#     def generate_bill(self):
#         print("Bill generated successfully.")

#     def update_order_status(self):
#         print("Order status updated.")


# class Customer(User):

#     def view_menu(self):
#         print("Displaying food menu.")

#     def place_order(self):
#         print("Order placed successfully.")

#     def view_order(self):
#         print("Displaying your orders.")

#     def view_bill(self):
#         print("Displaying your bill.")