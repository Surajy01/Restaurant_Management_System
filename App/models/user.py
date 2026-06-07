class User:
    def __init__(self, user_id, username, email, dob, address, password, role):
        self.user_id=user_id
        self.username=username
        self.email=email
        self.dob=dob
        self.address=address
        self.password=password
        self.role=role

    def display_profile(self):
        print("\n===== USER PROFILE =====")
        print(f"ID      : {self.user_id}")
        print(f"Name    : {self.username}")
        print(f"Email   : {self.email}")
        print(f"DOB     : {self.dob}")
        print(f"Address : {self.address}")
        print(f"Role    : {self.role}")


class Admin(User):

    def add_food(self):
        print("Food item added successfully.")

    def update_food(self):
        print("Food item updated successfully.")

    def delete_food(self):
        print("Food item deleted successfully.")

    def view_orders(self):
        print("Displaying all orders.")

    def manage_staff(self):
        print("Managing staff.")


class Staff(User):

    def view_menu(self):
        print("Displaying food menu.")

    def take_order(self):
        print("Order placed successfully.")

    def generate_bill(self):
        print("Bill generated successfully.")

    def update_order_status(self):
        print("Order status updated.")


class Customer(User):

    def view_menu(self):
        print("Displaying food menu.")

    def place_order(self):
        print("Order placed successfully.")

    def view_order(self):
        print("Displaying your orders.")

    def view_bill(self):
        print("Displaying your bill.")