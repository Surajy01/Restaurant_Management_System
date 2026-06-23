from app.menu.admin_menu import admin_menu
from app.menu.customer_menu import customer_menu
from app.menu.staff_menu import staff_menu
from app.auth.auth_service import AuthService
from app.domain.customer import Customer
from app.domain.admin import Admin
from app.domain.staff import Staff

def auth_menu():
    auth_service=AuthService()

    while True:
        print("\n┌────────────────────────────────────────────┐")
        print("│      🍽️  RESTAURANT MANAGEMENT SYSTEM  🍽️    │")
        print("├────────────────────────────────────────────┤")
        print("│       🔐  REGISTRATION & LOGIN MENU        │")
        print("├────────────────────────────────────────────┤")
        print("│  [1] 📝 Sign Up                            │")
        print("│  [2] 🔑 Sign In                            │")
        print("│  [3] 🚪 Exit                               │")
        print("└────────────────────────────────────────────┘")

        choice=input("👉 Enter Your Choice: ")

        if choice=="1":
            auth_service.sign_up()

        elif choice=="2":
            user=auth_service.sign_in()

            if user:
                if user["role"].lower()=="admin":
                    admin=Admin(
                        user_id=user["user_id"],
                        username=user["username"],
                        email=user["email"],
                        phone=user["phone"],
                        password=user["password"],
                        dob=user["dob"],
                        address=user["address"],
                        role=user["role"],
                    )
                    admin_menu(admin)
                    
                elif user["role"].lower()=="staff":
                    staff=Staff(
                        user_id=user["user_id"],
                        username=user["username"],
                        email=user["email"],
                        phone=user["phone"],
                        password=user["password"],
                        dob=user["dob"],
                        address=user["address"],
                        role=user["role"],
                        department=user["department"],
                        experience=user["experience"]
                    )
                    staff_menu(staff)

                elif user["role"].lower()=="customer":
                    customer=Customer(
                        user_id=user["user_id"],
                        username=user["username"],
                        email=user["email"],
                        phone=user["phone"],
                        password=user["password"],
                        dob=user["dob"],
                        address=user["address"],
                        role=user["role"],
                    )
                    customer_menu(customer)

        elif choice=="3":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")