#  name: Mohammad Sami manthoor. group <c>



dict1 = {
    "username": "aliahmed",
    "password": "12345678",
    "name": "Ali Ahmed",
    "email": "ali@gmail.com"
}

# Ask user for username and password (3 attempts allowed)
for i in range(3):
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == dict1["username"] and pwd == dict1["password"]:
        print("Login successful!")
        print(dict1)
        break
    else:
        print("Incorrect username or password. Try again.")

# If user failed 3 times → empty dict
else:
    dict1.clear()
    print("Too many wrong attempts. Dictionary emptied.")
    print(dict1)
