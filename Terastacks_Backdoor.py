from Dictionaries import payment_emails, \
    emails, withdrawals, user_purchases, market_purchases, stripe_account, \
    sales, deposits, user_countries
from TERACODES_Actions import *
import hashlib
import datetime


# ----------------------------------------- TERASTACKS BACKDOOR MENU ------------------------------------------
def terastacks_backdoor():
    global block_hash, next_block_hash
    print(f'''
********** TERASTACKS BACKDOOR ********** ''')
    print(f'''
🔶 - Teracode's Current Price: ${teracode_info["teracode_price"]}''')
    print('''
1. DATABASES
2. REFUND
3. INBOX
4. PAY THE TERACODE
5. VIEW THE BLOCKCHAIN
6. Log Out
''')
    while True:
        button = input("Button: ")
        try:
            if int(button) == 1:
                terastacks_databases()
                break
            if int(button) == 2:
                from Blockchain_Actions import terastacks_refunds
                terastacks_refunds()
                break
            if int(button) == 3:
                tera_inbox_fn()
                break
            if int(button) == 4:
                if teracode_info["teracode_price"] > 0:
                    print("❗️You currently can not pay the Teracode")
                    terastacks_backdoor()
                    break
                if teracode_info["teracode_price"] == 0:
                    teracode_info["teracode_price"] += 1
                    print("The Teracode has been paid.")
                    serial_numbers["block_number"] += 1
                    if serial_numbers["block_number"] == 1:
                        block_number = f'''Block {serial_numbers["block_number"]}'''
                        transaction = f'''Terastacks paid the Teracode | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                        block_data = block_number + " | " + transaction
                        block_hash = hashlib.sha256(block_data.encode()).hexdigest()
                        block = f'''{block_data} | {block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                    elif serial_numbers["block_number"] == 2:
                        block_number = f'''Block {serial_numbers["block_number"]}'''
                        transaction = f'''Terastacks paid the Teracode | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                        next_block_data = block_number + " | " + transaction + " | " + block_hash
                        next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                        block = f'''{next_block_data} | {next_block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                    elif serial_numbers["block_number"] > 2:
                        block_number = f'''Block {serial_numbers["block_number"]}'''
                        transaction = f'''Terastacks paid the Teracode | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                        next_block_data = block_number + " | " + transaction + " | " + next_block_hash
                        next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                        block = f'''{next_block_data} | {next_block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                    terastacks_backdoor()
                    break
            if int(button) == 5:
                print("********** BLOCKCHAIN **********")
                for key, value in blockchain.items():
                    print(key, '-', value)
                    print()
                leave = input("Type 'EXIT' to leave: ")
                if leave.upper() == "EXIT":
                    terastacks_backdoor()
            if int(button) == 6:
                import WelcomeMod
                WelcomeMod.welcome()
                break
            else:
                print("❗️Wrong button. Try again.")
        except ValueError:
            print("❗️Wrong button. Try again.")


# ----------------------------------------- TERASTACKS DATABASE ------------------------------------------
def terastacks_databases():
    print(f'''
********** TERASTACKS DATABASES ********** 
''')
    while True:
        print(f'''
        1. FIAT ACCOUNTS
        2. TERASTACKS ACCOUNTS
        3. STRIPE ACCOUNTS
        4. USER IDs
        5. USERs COUNTRIES
        6. EMAILS DATABASE
        7. PAYMENT EMAILS DATABASE
        8. DEPOSITS
        9. WITHDRAWALS
        10. TERACODES PURCHASES
        11. MARKET PURCHASES
        12. OTHER USER PURCHASES
        13. TERACODES SALES
        14. THE MARKET
        15. Exit ''')
        open_fn = input("Open #")
        try:
            if int(open_fn) == 1:
                print()
                print("💰 - FIAT ACCOUNTS:")
                for key, value in fiat_accounts.items():
                    print(key, '-', value)
            elif int(open_fn) == 2:
                print()
                print("🔶 - TERASTACKS ACCOUNTS:")
                for key, value in terastacks_accounts.items():
                    print(key, '-', value)
            elif int(open_fn) == 3:
                print()
                print("💳 - STRIPE ACCOUNTS:")
                for key, value in stripe_account.items():
                    print(key, '-', value)
            elif int(open_fn) == 4:
                print()
                print("🆔 - USER IDs:")
                for key, value in user_numbers.items():
                    print(key, '-', value)
            elif int(open_fn) == 5:
                print()
                print("📧 - USERs COUNTRIES:")
                for key, value in user_countries.items():
                    print(key, '-', value)
            elif int(open_fn) == 6:
                print()
                print("📧 - EMAILS DATABASE:")
                for key, value in emails.items():
                    print(key, '-', value)
            elif int(open_fn) == 7:
                print()
                print("📧 - PAYMENT EMAILS DATABASE:")
                for key, value in payment_emails.items():
                    print(key, '-', value)
            elif int(open_fn) == 8:
                print()
                print("➡️ - DEPOSITS:")
                for key, value in deposits.items():
                    print(key, '-', value)
            elif int(open_fn) == 9:
                print()
                print("⬅️ - WITHDRAWALS:")
                for key, value in withdrawals.items():
                    print(key, '-', value)
            elif int(open_fn) == 10:
                print()
                print("🔸 - TERACODES PURCHASES:")
                for key, value in terastacks_purchases.items():
                    print(key, '-', value)
            elif int(open_fn) == 11:
                print()
                print("🔸 - MARKET PURCHASES:")
                for key, value in market_purchases.items():
                    print(key, '-', value)
            elif int(open_fn) == 12:
                print()
                print("🔸 - OTHER USERS PURCHASES:")
                for key, value in user_purchases.items():
                    print(key, '-', value)
            elif int(open_fn) == 13:
                print()
                print("💵 - TERACODES SALES:")
                for key, value in sales.items():
                    print(key, '-', value)
            elif int(open_fn) == 14:
                print()
                print("📈 - THE MARKET:")
                for key, value in market.items():
                    print(key, '-', value)
            elif int(open_fn) == 15:
                terastacks_backdoor()
                break
            else:
                print("❗️ Wrong number! Try again.")
        except ValueError:
            print("❗️ Wrong answer! Try again.")


# ----------------------------------------- TERASTACKS INBOX ------------------------------------------
def tera_inbox_fn():
    print(f'''
********** INBOX (Purchase Orders) ********** 
''')
    if len(terastacks_inbox) == 0:
        print("You currently have 0 orders.")
    elif len(terastacks_inbox) != 0:
        print("💳 - PURCHASE ORDERS:")
        for key, value in terastacks_inbox.items():
            print(key, '-', value)
    print('''
1. ACCEPT AN OFFER
2. DECLINE AN OFFER
3. Exit
''')
    while True:
        menu_button = input("Button: ")
        try:
            if int(menu_button) == 3:
                terastacks_backdoor()
                break
            if int(menu_button) == 2:
                offer_decline = int(input("Which Offer would you like to decline? #"))
                terastacks_inbox.pop(offer_decline)
            if int(menu_button) == 1:
                while True:
                    order_number = int(input("Which Offer would you like to accept? #"))
                    if order_number not in purchase_orders:
                        print("❗️This offer does not exist. Try again.")
                    else:
                        while True:
                            user = input("Please type the username of the user who sent the offer: ")
                            for key, value in terastacks_inbox.items():
                                if user not in value:
                                    print("❗️The username doesn't match the purchase offer.")
                            else:
                                while True:
                                    teracodes_amount = int(input("How many Teracodes are you willing to buy? 🔸"))
                                    teracode_value = teracodes_amount * teracode_info["teracode_price"]
                                    if fiat_accounts["terastacks"] < teracode_value:
                                        print("❗️You don't have enough FIAT to purchase these Teracodes.")
                                        tera_inbox_fn()
                                        break
                                    else:
                                        print()
                                        print(
                                            f'''You will buy {teracodes_amount}🔸 from {user} for a return of ${teracode_value}.''')
                                        print()
                                        while True:
                                            confirm_sale = input("Do you wish to proceed? [Y/N] ")
                                            if confirm_sale.upper() == "N":
                                                tera_inbox_fn()
                                                break
                                            if confirm_sale.upper() == "Y":
                                                if terastacks_accounts[user] < teracodes_amount:
                                                    print(
                                                        "❗️The purchase order could not be completed. Try again another time.")
                                                else:
                                                    fiat_accounts[user] += teracode_value
                                                    fiat_accounts["terastacks"] -= teracode_value
                                                    terastacks_accounts[user] -= teracodes_amount
                                                    terastacks_accounts["terastacks"] += teracodes_amount
                                                    serial_numbers["sale_number"] += 1
                                                    sales[serial_numbers[
                                                        "sale_number"]] = f'''{user} sold {teracodes_amount}🔸 for ${teracode_value} to Terastacks '''
                                                    serial_numbers["purchase_number"] += 1
                                                    terastacks_purchases[serial_numbers[
                                                        "purchase_number"]] = f'''Terastacks purchased {teracodes_amount}🔸 for ${teracode_value} from {user} '''
                                                    print()
                                                print(
                                                    f'''✅ The purchase order has been completed! We will notify {user}.''')
                                                terastacks_inbox.pop(order_number)
                                                tera_inbox_fn()
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")
