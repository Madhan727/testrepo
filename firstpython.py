USERNAME = "admin"
PASSWORD = "1234"
user_name = input("Enter username: ")
user_password = input("Enter password: ")

if user_name == USERNAME and user_password == PASSWORD:
    print("✅ Login Successful!")
else:
    print("❌ Invalid username or password")
