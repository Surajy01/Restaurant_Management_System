import json

FILE_PATH="App/database/signup.json"


def signin():
    print("\n===== SIGN IN =====")

    email=input("Enter Email: ")
    password=input("Enter Password: ")

    try:
        with open(FILE_PATH, "r") as file:
            users=json.load(file)
    except:
        users=[]

    for user in users:
        if user["email"]==email and user["password"]==password:
            print(f"\nWelcome {user['username']}")
            print(f"Logged in as {user['role']}")
            return user

    print("Invalid Email or Password!")
    return None