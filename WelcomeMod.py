from Dictionaries import terastacks_accounts, fiat_accounts, serial_numbers, user_numbers, emails, passwords, payment_emails, account_creation, user_countries, ISO3166
import bcrypt
import Terastacks_Backdoor
import datetime


# ----------------------------------------- WELCOME PAGE ------------------------------------------
def welcome():
    print('''
********** WELCOME TO TERASTACKS ********** 

1 - SIGN UP
2 - SIGN IN
3 - Exit
''')
    button = input("Button: ")
    try:
        if int(button) == 1:
            sign_up()
        if int(button) == 2:
            sign_in()
        if int(button) == 3:
            exit()
        else:
            print("❗️Wrong button! Try again.")
            welcome()
    except ValueError:
        print("❗️Wrong button! Try again.")
        welcome()


# ----------------------------------------- SIGN UP PAGE ------------------------------------------
def sign_up():
    print('''
********** SIGN UP PAGE ********** 

      - Create your account - 
''')
    while True:
        username = input("Username: ")
        if username in terastacks_accounts:
            print("❗️Username already taken.")
        else:
            fiat_accounts[username] = 0
            terastacks_accounts[username] = 0
            serial_numbers["user_id"] += 1
            user_numbers[username] = f'''User{serial_numbers["user_id"]}'''
            break
    while True:
        country = str(input("Country: "))
        if country.upper() not in ISO3166.values():
            print("❗️ Country not in database! Try again.")
        else:
            user_countries[username] = country.upper()
            break
    while True:
        email = input("Email: ")
        if email in emails:
            print("❗️This email address is already registered.")
        elif "@" and "." not in email:
            print("❗️ Invalid Email! Try again.")
        else:
            emails[username] = email
            payment_emails[username] = email
            break
    while True:
        password = input("Password: ").encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        passwords[username] = hashed
        confirm_password = input("Confirm Password: ").encode("utf-8")
        if bcrypt.checkpw(confirm_password, passwords[username]):
            print()
            print("🔶 WELCOME TO TERASTACKS! 🔶")
            account_creation[username] = datetime.datetime.now()
            import Homepage_Menu
            Homepage_Menu.homepage(username)
            break
        else:
            print("❗️Wrong confirmation! Try again.")


# ----------------------------------------- SIGN IN PAGE ------------------------------------------
def sign_in():
    print('''
********** SIGN IN PAGE ********** 
    ''')
    while True:
        username = input("Username: ")
        if username not in terastacks_accounts:
            print(f'''❗️User not found!

1. Try again
2. Register 
''')
            sign_in_option = input("Button: ")
            try:
                if int(sign_in_option) == 1:
                    sign_in()
                if int(sign_in_option) == 2:
                    sign_up()
                    break
                else:
                    print("❗️Wrong button! Try again.")
            except ValueError:
                print("❗️Wrong button! Try again.")
        else:
            if username == "terastacks":
                Terastacks_Backdoor.terastacks_backdoor()
        if username in terastacks_accounts:
            break
    while True:
        password = input("Password: ").encode("utf-8")
        if bcrypt.checkpw(password, passwords[username]):
            import Homepage_Menu
            Homepage_Menu.homepage(username)
            break
        else:
            print("❗️Wrong password! Try again.")


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RUN THE APPLICATION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
welcome()
