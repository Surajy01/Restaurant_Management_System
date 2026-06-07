import json
import os
import uuid
from App.models.user import User

FILE_PATH = "App/database/signup.json"

os.makedirs("App/database", exist_ok=True)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump([], file)

def signup():
    print("\n===== SIGN UP =====")

    user_id=str(uuid.uuid4().hex)[:8]
    username=input("Enter Username: ")
    email=input("Enter Email: ")
    dob=input("Enter DOB (DD/MM/YYYY): ")
    address=input("Enter Address: ")
    password=input("Enter Password: ")
    phoneNo=input("Enter Phone Number: ")
    role=input("Enter Role (Admin/Staff/Customer): ")

    try:
        with open(FILE_PATH, "r") as file:
            users=json.load(file)
    except:
        users=[]

    # Check duplicate email
    for user in users:
        if user["email"]==email:
            print("Email already exists!")
            return

    new_user={
        "user_id": user_id,
        "username": username,
        "email": email,
        "dob": dob,
        "address": address,
        "password": password,
        "phoneNo": phoneNo,
        "role": role
    }

    users.append(new_user)

    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)

    print("Signup Successful!")