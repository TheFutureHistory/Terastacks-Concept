import bcrypt

passwords = {}

def sign_up():
    username = input("Username: ")
    password = input("Password: ").encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    passwords[username] = hashed
    print(passwords)
    sign_in()


def sign_in():
    while True:
        username = input("Username: ")
        if username in passwords:
            password = input("Password: ").encode("utf-8")
            if bcrypt.checkpw(password, passwords[username]):
                print("It matches!")
            else:
                print("didn't match")
        else:
            print("user not found.")


sign_up()





