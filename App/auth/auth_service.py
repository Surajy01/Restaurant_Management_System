import uuid
from app.utils.file_handler import read_data, write_data
from getpass import getpass
import re
from datetime import datetime
from app.domain.user import User
# import hashlib

FILE_PATH="app/database/sign_up.json"

class AuthService:

    def sign_up(self):

        users=read_data(FILE_PATH)

        print("\n===== 📝 SIGN UP =====")

        user_id=str(uuid.uuid4().hex[:8])
        username=input("Enter username: ").strip()
            
        # Email Validation
        while True:
            email=input("Enter email: ").strip()

            # Check if email already exists
            for user in users:
                if user["email"].lower()==email.lower():
                    print("\nEmail already exists. Please use a different email.")
                    return

            email_pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

            if re.match(email_pattern, email):
                break

            print("Invalid email format. Please try again.")

        # Phone Validation
        while True:
            phone=input("Enter phone number: ").strip()

            if phone.isdigit() and len(phone)==10:
                break

            print("Phone number must contain exactly 10 digits.")

        # Password Validation
        while True:
            password=getpass("Enter password: ")

            if (
                len(password)>=8
                and re.search(r"[A-Z]", password)
                and re.search(r"[a-z]", password)
                and re.search(r"\d", password)
                and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
            ):
                break

            print(
                "Password must be at least 8 characters long and contain:\n"
                "- 1 uppercase letter\n"
                "- 1 lowercase letter\n"
                "- 1 number\n"
                "- 1 special character"
            )

        # Date of Birth Validation
        while True:
            dob=input("Enter date of birth (DD-MM-YYYY): ").strip()

            try:
                datetime.strptime(dob, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY.")

        address=input("Enter address: ").strip()

        # Role Validation
        while True:
            role=input("Enter role (admin/staff/customer): ").strip().lower()

            if role in ["admin", "staff", "customer"]:
                break

            print("Invalid role. Please enter admin, staff, or customer.")

        department=""
        experience=""

        # Staff-specific fields
        if role=="staff":

            while True:
                department=input("Enter department: ").strip()

                if department:
                    break

                print("Department cannot be empty.")

            while True:
                experience=input("Enter experience (in years): ").strip()

                if experience.isdigit() and int(experience)>=0:
                    break

                print("Experience must be a valid non-negative number.")


        # user_data={
        #     "user_id": user_id,
        #     "username": username,
        #     "email": email,
        #     "phone": phone,
        #     "password": password,  # Consider hashing in production
        #     "dob": dob,
        #     "address": address,
        #     "role": role,
        #     "department": department,
        #     "experience": experience
        # }

        new_user=User(
            user_id=user_id,
            username=username,
            email=email,
            phone=phone,
            password=password,
            dob=dob,
            address=address,
            role=role,
            department=department,
            experience=experience
        )

        users.append(new_user.dict())
        write_data(FILE_PATH, users)

        print("\nUser registered successfully!")



    def sign_in(self):

        print("\n===== 🔑 SIGN IN =====")

        email=input("Enter email: ").strip()
        password=getpass("Enter password: ")

        users=read_data(FILE_PATH)

        for user in users:
            if(user["email"].lower()==email.lower()and user["password"]==password):
                print("\nSign in successful!")
                print(f"Welcome {user['username']}, "f"Signed in as {user['role']}")
                return user

        print("\nInvalid email or password. Please try again.")
        return None
    