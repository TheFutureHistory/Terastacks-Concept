from Dictionaries import terastacks_balance, market, fiat_accounts, teracode_info, terastacks_accounts, serial_numbers, \
    terastacks_purchases, user_numbers, blockchain, purchase_orders, account_balance, transfers, terastacks_inbox
import hashlib
import datetime


# ----------------------------------------- TERACODES MENU ------------------------------------------
def teracodes(username):
    print(f'''
********** TERACODES MENU ********** ''')
    terastacks_balance()
    print(f'''
********** THE MARKET  ********** ''')
    for key, value in market.items():
        print(key, ':', value)
    print(f'''
1. BUY TERACODES
2. SELL TERACODES
3. TRANSFER TERACODES 
4. Exit
    ''')
    while True:
        button = input("Button: ")
        try:
            if int(button) == 1:
                from Blockchain_Actions import purchase_teracodes
                purchase_teracodes(username)
                break
            if int(button) == 2:
                sell_teracodes(username)
                break
            if int(button) == 3:
                transfer_teracodes(username)
                break
            if int(button) == 4:
                import Homepage_Menu
                Homepage_Menu.homepage(username)
                break
            else:
                print("❗️Wrong button. Try again.")
        except ValueError:
            print("❗️Wrong Button. Try again.")


# ----------------------------------------- SELL TERACODES PAGE ------------------------------------------
def sell_teracodes(username):
    print('''
********** SELL TERACODES ********** ''')
    terastacks_balance()
    account_balance(username)
    print()
    if terastacks_accounts[username] < 0:
        print("❗️You currently have 0 Teracodes to sell.")
        teracodes(username)
    else:
        print('''
1. SELL TERACODES
2. Exit
''')
        while True:
            button = input("Button: ")
            try:
                if int(button) == 2:
                    teracodes(username)
                    break
                if int(button) == 1:
                    while True:
                        teracode_amount = int(input("How many Teracodes would you like to sell? 🔸 "))
                        teracode_value = teracode_amount * teracode_info["teracode_price"]
                        if teracode_amount > terastacks_accounts[username]:
                            print(f'❗️ You currently have {terastacks_accounts[username]}🔸 to sell.')
                            sell_teracodes(username)
                        else:
                            print(f'''Who do you wish to sell to? 
1. Terastacks
2. The Market
                    ''')
                            while True:
                                button = input("Button: ")
                                try:
                                    if int(button) == 1:
                                        print()
                                        print(
                                            f'''❕ You want to sell {teracode_amount}🔸 for ${teracode_value} to Terastacks.''')
                                        print()
                                        print(
                                            "❕ * Note that once the offer has been sent, the value of those specific Teracodes will be frozen *")
                                        print()
                                        while True:
                                            proceed = input("Do you wish to proceed? [Y/N]")
                                            if proceed.upper() == "N":
                                                sell_teracodes(username)
                                            if proceed.upper() == "Y":
                                                serial_numbers["tera_inbox_number"] += 1
                                                terastacks_inbox[serial_numbers[
                                                    "tera_inbox_number"]] = f'''{username} wants to sell Terastacks {teracode_amount}🔸 for ${teracode_value}'''
                                                print()
                                                print(
                                                    f'''✅ You have successfully sent your offer! We will notify Terastacks.''')
                                                teracodes(username)
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
                                    if int(button) == 2:
                                        import MARKET_Actions
                                        MARKET_Actions.market_sale(username)
                                        break
                                    else:
                                        print("❗️Wrong button! Try again.")
                                except ValueError:
                                    print("❗️Wrong button! Try again.")
                else:
                    print("❗️Wrong button! Try again.")
            except ValueError:
                print("❗️Wrong button! Try again.")


# ----------------------------------------- TRANSFER TERACODES PAGE ------------------------------------------
def transfer_teracodes(username):
    print('''
********** TRANSFER TERACODES ********** ''')
    account_balance(username)
    print('''
1. TRANSFER TERACODES
2. Exit
''')
    while True:
        button = input("Button: ")
        try:
            if int(button) == 2:
                teracodes(username)
                break
            if int(button) == 1:
                print()
                while True:
                    teracodes_amount = int(input("How many Teracodes would you like to transfer? 🔸"))
                    if teracodes_amount > terastacks_accounts[username]:
                        print(f'''❗️You currently have {terastacks_accounts[username]}🔸 to transfer.''')
                        transfer_teracodes(username)
                        break
                    else:
                        while True:
                            print()
                            teracodes_receiver = input("Enter the Username you want to transfer to: ")
                            if teracodes_receiver not in terastacks_accounts:
                                print("❗️User not found. Try again.")
                                transfer_teracodes(username)
                                break
                            else:
                                print()
                                print(f'''❕ You will send {teracodes_amount}🔸 to {teracodes_receiver}.''')
                                print()
                                while True:
                                    proceed = input("Do you wish to proceed? [Y/N]")
                                    if proceed.upper() == "N":
                                        transfer_teracodes(username)
                                    if proceed.upper() == "Y":
                                        terastacks_accounts[username] -= teracodes_amount
                                        terastacks_accounts[teracodes_receiver] += teracodes_amount
                                        serial_numbers["transfers_number"] += 1
                                        transfers[serial_numbers[
                                            "transfers_number"]] = f'''{username} sent {teracodes_amount}🔸 to {teracodes_receiver}'''
                                        print()
                                        print(
                                            f'''✅ You successfully sent {teracodes_amount}🔸 to {teracodes_receiver}!''')
                                        teracodes(username)
                                        break
                                    else:
                                        print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")
