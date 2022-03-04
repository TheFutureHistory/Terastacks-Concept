from Dictionaries import emails, user_numbers, terastacks_accounts, fiat_accounts, passwords, payment_emails, account_creation, user_countries
import datetime


# ----------------------------------------- SETTINGS MENU ------------------------------------------
def settings(username):
    print(f'''
********** SETTINGS ********** 

1. USERNAME: {username}
2. ID NUMBER: {user_numbers[username]}
3. EMAIL: {emails[username]}
4. PAYMENT EMAIL: {payment_emails[username]}
5. PASSWORD: PRIVATE
6. COUNTRY: {user_countries[username]}
7. ACCOUNT CREATED: {account_creation[username]}

8. * MODIFY A SETTING
9. * DELETE ACCOUNT
10. Exit
''')
    while True:
        number = input("Button: ")
        try:
            if int(number) == 10:
                import Profile_Menu
                Profile_Menu.profile(username)
            if int(number) == 9:
                from Blockchain_Actions import delete_account
                delete_account(username)
            if int(number) == 8:
                while True:
                    button = int(input("Which setting # would you like to modify? "))
                    try:
                        if int(button) == 1:
                            while True:
                                print()
                                new_username = input("NEW USERNAME: ")
                                if new_username in terastacks_accounts:
                                    print("❗️Username already taken.")
                                else:
                                    fiat_accounts[new_username] = fiat_accounts.pop(username)
                                    terastacks_accounts[new_username] = terastacks_accounts.pop(username)
                                    emails[new_username] = emails.pop(username)
                                    passwords[new_username] = passwords.pop(username)
                                    payment_emails[new_username] = payment_emails.pop(username)
                                    user_numbers[new_username] = user_numbers.pop(username)
                                    user_countries[new_username] = user_countries.pop(username)
                                    print()
                                    print(
                                        f'''✅ You successfully changed your username from {username} to {new_username}!''')
                                    settings(new_username)
                                    break
                        if int(button) == 3:
                            while True:
                                print()
                                new_email = input("NEW EMAIL: ")
                                if new_email in emails:
                                    print("❗️This email address is already registered.")
                                elif "@" and "." not in new_email:
                                    print("❗️This is an invalid email address.")
                                else:
                                    print()
                                    print(
                                        f'''✅ You successfully changed your email address from {emails[username]} to {new_email}!''')
                                    emails[username] = new_email
                                    settings(username)
                                    break
                        if int(button) == 4:
                            while True:
                                print()
                                new_p_email = input("NEW PAYMENT EMAIL: ")
                                if new_p_email in payment_emails:
                                    print("❗️This email address is already registered.")
                                elif "@" and "." not in new_p_email:
                                    print("❗️This is an invalid email address.")
                                else:
                                    print()
                                    print(
                                        f'''✅ You successfully changed your email address from {payment_emails[username]} to {new_p_email}!''')
                                    payment_emails[username] = new_p_email
                                    settings(username)
                                    break
                        if int(button) == 5:
                            while True:
                                password = input("Current Password:  ")
                                if password != passwords[username]:
                                    print("❗️Wrong Password! Try Again")
                                else:
                                    new_password = input("NEW PASSWORD: ")
                                    passwords[username] = new_password
                                    print()
                                    print("✅ You successfully changed your password!")
                                    settings(username)
                                    break
                        if int(button) == 6:
                            new_country = str(input("NEW COUNTRY: "))
                            user_countries[username] = new_country.upper()
                            print()
                            print(f"✅ You successfully changed your country to {new_country.upper()}!")
                            settings(username)
                            break
                    except ValueError:
                        print("❗️Wrong button! Try again.")
            else:
                print("❗️ Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")
