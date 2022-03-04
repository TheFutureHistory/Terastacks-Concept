# !!!!! THIS PAGE IS FOR: Deposits, Withdrawals, Transfer of FIAT !!!!!
from Dictionaries import *
from Profile_Menu import profile
import bcrypt
import datetime
import moneyed
from forex_python.converter import CurrencyRates


# ----------------------------------------- DEPOSIT PAGE ------------------------------------------
def deposits_fn(username):
    print('''
********** DEPOSIT ********** ''')
    account_balance(username)
    print()
    print('$ --- CURRENCY CONVERTER --- $')
    while True:
        country_name = user_countries[username]
        for currency, data in moneyed.CURRENCIES.items():
            if country_name.upper() in data.countries:
                print(f'''❕YOUR CURRENT CURRENCY: {currency}''')
                print("❕You can change the currency's country in settings❕")
                break
        # FINDS THE RATE OF THE CONVERSION
        print()
        amount = int(input(f"Convert to USD: {currency}$"))
        print()
        print(f'''❕Converting {currency} into USD. Please wait.❕''')
        c = CurrencyRates()
        rate = round(c.get_rate('USD', f'{currency}'), 2)
        result = amount / rate
        print()
        print(f'''Official rate: {rate}''')
        print(f"Total: {currency}${amount} = USD${round(result)} ")
        break
        # CONTINUE OR TRY AGAIN
    while True:
        print('''
1. CONVERT AGAIN [CA]
2. CONTINUE TRANSACTION [CT]''')
        print()
        try:
            choice = input("Button #")
            if int(choice.upper()) == 1:
                True
                deposits_fn(username)
            if int(choice.upper()) == 2:
                print("❕Enter a USD amount without decimals❕")
                break
            else:
                print("❗Wrong button! Try again.")
        except ValueError:
                print("❗️Wrong answer! Try again.")
    print()
    amount = int(input("How much do you want to deposit? USD$"))
    if amount == 0:
        profile(username)
    else:
        print('''
        ********** CREDIT CARD INFORMATION ********** ''')
        print('---------- ❕We do not save your CC information | More info at FAQ❕ ----------')
        print()
        while True:
            credit_number = str(input("Credit Card Number: "))
            if len(credit_number) != 16:
                print("❗️Invalid Card Number! Try again.")
            else:
                break
        card_name = str(input("Name on Card: ")).upper()
        expiry_date = input("Expiry Date [M/Y]: ")
        while True:
            security_code = str(input("Security Code: "))
            if len(security_code) != 3:
                print("❗️Invalid Security Code! Try again.")
            else:
                break
        print(f'''❕ Your Credit Card will be charged ${amount} USD.''')
        while True:
            print()
            conf_pass = input("Enter your password to confirm the transaction: ").encode("utf-8")
            if bcrypt.checkpw(conf_pass, passwords[username]):
                fiat_accounts[username] += amount
                print()
                print(f'''✅ You successfully deposited ${amount} in your account! ''')
                stripe_account["terastacks"] += amount
                serial_numbers["deposits_number"] += 1
                deposits[serial_numbers[
                    "deposits_number"]] = f'''{username} deposited ${amount} | {datetime.datetime.now()}'''
                profile(username)
                break
            else:
                print("❗️Wrong confirmation! Try again.")


# ----------------------------------------- WITHDRAWAL PAGE ------------------------------------------
def withdrawals_fn(username):
    print('''
********** WITHDRAWAL ********** ''')
    account_balance(username)
    print()
    if fiat_accounts[username] == 0:
        print("❗️Your FIAT account balance is currently at $0.")
        profile(username)
    else:
        while True:
            amount = int(input("How much do you want to withdraw? $"))
            print('$ --- CURRENCY CONVERTER --- $')
            print()
            while True:
                country_name = user_countries[username]
                for currency, data in moneyed.CURRENCIES.items():
                    if country_name.upper() in data.countries:
                        print(f'''❕YOUR CURRENT CURRENCY: {currency}''')
                        print("❕You can change the currency's country in settings❕")
                        break
                # FINDS THE RATE OF THE CONVERSION
                print()
                print(f'''❕Converting USD into {currency}. Please wait.❕''')
                c = CurrencyRates()
                rate = round(c.get_rate('USD', f'{currency}'), 2)
                result = amount * rate
                print()
                print(f'''Official rate: {rate}''')
                print(f"Total: USD${amount} = {currency}${round(result)} ")
                break
                # CONTINUE OR TRY AGAIN
            while True:
                print('''
            1. CONVERT AGAIN [CA]
            2. CONTINUE TRANSACTION [CT]''')
                print()
                try:
                    choice = input("Button #")
                    if int(choice.upper()) == 1:
                        True
                        withdrawals_fn(username)
                    if int(choice.upper()) == 2:
                        break
                    else:
                        print("❗Wrong button! Try again.")
                except ValueError:
                    print("❗️Wrong answer! Try again.")
            print()
            if amount > fiat_accounts[username]:
                print(f'''❗️The maximum you can currently withdraw is ${fiat_accounts[username]}.''')
            else:
                if username not in payment_emails:
                    print("❗️ You need to create a payment email in your settings.")
                    import Setting_Menu
                    Setting_Menu.settings(username)
                    break
                else:
                    print(f'''❕ We will send the ${amount} USD to {payment_emails[username]}.''')
                    print("-You can change the payment email in your settings-")
                    break
        button = str(input("Do you wish to proceed? [Y/N] "))
        if button.upper() == "Y":
            fiat_accounts[username] -= amount
            print()
            print(f'''✅ You successfully withdrew ${amount} from your account!''')
            print("You will receive your funds in 2-5 business days.")
            serial_numbers["withdrawals_number"] += 1
            withdrawals[
                serial_numbers["withdrawals_number"]] = f'''{username} withdrew ${amount} | {datetime.datetime.now()}'''
            profile(username)
        elif button.upper() == "N":
            profile(username)


# ----------------------------------------- TRANSFER PAGE ------------------------------------------
def transfer(username):
    print('''
********** TRANSFER FIAT ********** ''')
    account_balance(username)
    print()
    if fiat_accounts[username] == 0:
        print("❗️Your FIAT account balance is currently at $0.")
        profile(username)
    else:
        while True:
            amount = int(input("How much would you like to transfer? $"))
            if amount > fiat_accounts[username]:
                print(f'''❗️The maximum you can currently transfer is ${fiat_accounts[username]}.''')
            else:
                while True:
                    print()
                    receiver = input("Which user would you like to transfer to: ")
                    if receiver not in terastacks_accounts:
                        print("❗️User not found.")
                    else:
                        fiat_accounts[username] -= amount
                        fiat_accounts[receiver] += amount
                        print()
                        print(f'''✅ You successfully sent ${amount} to {receiver}!''')
                        serial_numbers["transfers_number"] += 1
                        transfers[serial_numbers[
                            "transfers_number"]] = f'''{username} sent ${amount} to {receiver} | {datetime.datetime.now()}'''
                        profile(username)
                        break
