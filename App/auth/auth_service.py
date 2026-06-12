import uuid
from App.utils.file_handler import read_data, write_data

FILE_PATH = "App/database/signup.json"

class AuthService:

    def sign_up(self):
        print("\n===== SIGN UP =====")
        user_id=str(uuid.uuid4().hex[:8])
        username=input("Enter username: ")
        email=input("Enter email: ")
        phone=input("Enter phone number: ")
        password=input("Enter password: ")
        dob=input("Enter date of birth (DD-MM-YYYY): ")
        address=input("Enter address: ")
        role=input("Enter role (admin/staff/customer): ")
        department=input("Enter department: ")
        experience=input("Enter experience (in years): ")

        users=read_data(FILE_PATH)

        for user in users:
            if user["email"]==email:
                print("\nEmail already exists. Please try again with a different email.")
                return

        user_data={
            "user_id": user_id,
            "username": username,
            "email": email,
            "phone": phone,
            "password": password,
            "dob": dob,
            "address": address,
            "role": role,
            "department": department,
            "experience": experience
        }

        users.append(user_data)

        write_data(FILE_PATH,users)

        print("\nUser registered successfully!")

    def sign_in(self):
        print("\n===== SIGN IN =====")

        email=input("Enter email: ")
        password=input("Enter password: ")

        users=read_data(FILE_PATH)

        for user in users:
            if user["email"]==email and user["password"]==password:
                print("\nSign in successful!")
                print(f"Welcome {user['username']}, Sign in as {user['role']}")
                return user

        print("\nInvalid email or password. Please try again.")
        return None
        