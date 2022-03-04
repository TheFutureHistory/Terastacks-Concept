import hashlib
import bcrypt
import datetime

# ----------------------------------------- DICTIONARIES ------------------------------------------

teracode_info = {
    "teracode_price": 1
}

fiat_accounts = {
    "terastacks": 0,
    "GODMODE": 0
}

terastacks_accounts = {
    "terastacks": 100,
    "GODMODE": 0
}

stripe_account = {
    "terastacks": 0,
}

user_numbers = {}

serial_numbers = {
    "deposits_number": 0,
    "withdrawals_number": 0,
    "transfers_number": 0,
    "purchase_orders_number": 0,
    "purchase_number": 0,
    "sale_number": 0,
    "tera_inbox_number": 0,
    "blockchain_sn": 0,
    "block_number": 0,
    "user_id": 0,
}

emails = {
    "GODMODE": "GODMODE"
}
passwords = {
    "terastacks": "terastacks",
    "GODMODE": "GODMODE"
}
refund_demands = {}
refunded = {}
deposits = {}
withdrawals = {}
transfers = {}
purchase_orders = {}
terastacks_purchases = {}
market_purchases = {}
user_purchases = {}
sales = {}
market = {}
terastacks_inbox = {}
blockchain = {}


# ----------------------------------------- GENERAL FUNCTIONS ------------------------------------------
def account_balance(username):
    print(f"FIAT ACCOUNT: ${fiat_accounts[username]} ")
    print(f'''TERASTACKS ACCOUNT: {terastacks_accounts[username]}🔸''')


def terastacks_balance():
    print(f'''🔶 - TERASTACKS TERACODES: {terastacks_accounts["terastacks"]}🔸''')
    print(f'''🔸 - TERACODE CURRENT PRICE: ${teracode_info["teracode_price"]}''')


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
        email = input("Email: ")
        if email in emails:
            print("❗️This email address is already registered.")
        elif "@" and "." not in email:
            print("Invalid Email! Try again.")
        else:
            emails[username] = email
            break
    while True:
        password = input("Password: ").encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        passwords[username] = hashed
        confirm_password = input("Confirm Password: ").encode("utf-8")
        if bcrypt.checkpw(confirm_password, passwords[username]):
            homepage(username)
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
                terastacks_backdoor()
        if username in terastacks_accounts:
            break
    while True:
        password = input("Password: ").encode("utf-8")
        if bcrypt.checkpw(password, passwords[username]):
            homepage(username)
            break
        else:
            print("❗️Wrong password! Try again.")


# ----------------------------------------- HOMEPAGE MENU ------------------------------------------
def homepage(username):
    print('''
********** HOMEPAGE ********** ''')
    terastacks_balance()
    print('''
1 - PROFILE
2 - TERACODES
3 - THE MARKET
4 - THE BLOCKCHAIN 
5 - Log Out
''')
    while True:
        try:
            button = input("Button: ")
            if int(button) == 1:
                profile(username)
            if int(button) == 2:
                teracodes(username)
            if int(button) == 3:
                the_market(username)
            if int(button) == 4:
                the_blockchain(username)
            if int(button) == 5:
                welcome()
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


# ----------------------------------------- PROFILE MENU ------------------------------------------
def profile(username):
    print(f'''
********** {username} PROFILE **********''')
    account_balance(username)
    print(f'''
1 - DEPOSIT
2 - WITHDRAWALS
3 - TRANSFER FIAT
4 - REFUND     
5 - PURCHASE ORDERS
6 - HISTORY 
7 - SETTINGS
8 - Home 
''')
    while True:
        try:
            button = input("Button: ")
            if int(button) == 1:
                deposits_fn(username)
            if int(button) == 2:
                withdrawals_fn(username)
            if int(button) == 3:
                transfer(username)
            if int(button) == 4:
                refund_fn(username)
            if int(button) == 5:
                users_purchase_orders(username)
            if int(button) == 6:
                personal_history(username)
            if int(button) == 7:
                settings(username)
            if int(button) == 8:
                homepage(username)
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


# ----------------------------------------- DEPOSIT PAGE ------------------------------------------
def deposits_fn(username):
    print('''
********** DEPOSIT ********** ''')
    account_balance(username)
    print()
    amount = int(input("How much do you want to deposit? USD$"))
    if amount == 0:
        profile(username)
    else:
        print('''
        ********** CREDIT CARD INFORMATION ********** ''')
        print('---------- We do not save your information | More info at FAQ ----------')
        while True:
            credit_number = int(input("Credit Card Number: "))
            if credit_number < 16:
                print("❗️Invalid Card Number! Try again.")
            break
        card_name = str(input("Name on Card: ")).upper()
        expiry_date = input("Expiry Date [M/Y]: ")
        while True:
            security_code = int(input("Security Code: "))
            if security_code < 3:
                print("❗️Invalid Security Code! Try again.")
            break
        print(f'''Your Credit Card will be charged ${amount} USD.''')
        while True:
            conf_pass = input("Enter your password to confirm the transaction: ").encode("utf-8")
            if bcrypt.checkpw(conf_pass, passwords[username]):
                fiat_accounts[username] += amount
                print()
                print(f'''You successfully deposited ${amount} in your account!''')
                stripe_account["terastacks"] += amount
                serial_numbers["deposits_number"] += 1
                deposits[serial_numbers["deposits_number"]] = f'''{username} deposited ${amount}'''
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
            if amount > fiat_accounts[username]:
                print(f'''❗️The maximum you can currently withdraw is ${fiat_accounts[username]}.''')
            else:
                fiat_accounts[username] -= amount
                print()
                print(f'''You successfully withdrew ${amount} from your account!''')
                serial_numbers["withdrawals_number"] += 1
                withdrawals[serial_numbers["withdrawals_number"]] = f'''{username} withdrew ${amount}'''
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
                        print(f'''You successfully sent ${amount} to {receiver}!''')
                        serial_numbers["transfers_number"] += 1
                        transfers[serial_numbers["transfers_number"]] = f'''{username} sent ${amount} to {receiver}'''
                        profile(username)
                        break


# ----------------------------------------- REFUND PAGE ------------------------------------------
def refund_fn(username):
    print('''
**********  REFUNDS **********
''')
    print(f'''* Note that only purchases bought from Terastacks Vault can be refunded 
* Note that any refund will decrease the Teracode's value by $1 
* Note that you will be refunded at same purchasing price 
''')
    print(f'''1. SEND REFUND REQUEST
2. VIEW REFUNDS
3. Exit
''')
    while True:
        button = input("Button: ")
        try:
            if int(button) == 3:
                profile(username)
                break
            if int(button) == 2:
                print()
                print("🔶 - TERASTACKS REFUNDS:")
                for key, value in refunded.items():
                    if value.startswith(username):
                        print(key, '-', value)
                        print()
                while True:
                    print()
                    leave = input('''Type "EXIT" to leave: ''')
                    try:
                        if leave.upper() == "EXIT":
                            refund_fn(username)
                            break
                        else:
                            print("❗️Wrong answer! Try again.")
                    except ValueError:
                        print("❗️Wrong answer! Try again.")
                print()
            if int(button) == 1:
                print()
                print("🔶 - TERASTACKS PURCHASES:")
                for key, value in terastacks_purchases.items():
                    if value.startswith(username):
                        print(key, '-', value)
                print()
                transaction_number = int(input("Which Transaction would you like refunded? #"))
                if transaction_number not in terastacks_purchases:
                    print("❗️This order does not exist.")
                    refund_fn(username)
                else:
                    transaction_demand = terastacks_purchases[transaction_number]
                    print()
                    print(f'''You wish to be refunded the Transaction #{transaction_number}: {transaction_demand}''')
                    print()
                while True:
                    transaction_demand = terastacks_purchases[transaction_number]
                    proceed = input("Do you wish to proceed? [Y/N] ")
                    if proceed.upper() == "N":
                        refund_fn(username)
                        break
                    if proceed.upper() == "Y":
                        refund_demands[transaction_number] = transaction_demand
                        print()
                        print(
                            f"Your refund demand for Transaction #{transaction_number} has been sent to Terastacks.")
                        refund_fn(username)
                        break
                    else:
                        print("❗️Wrong Answer! Try again.")
            else:
                print("❗️Wrong Number! Try again.")
        except ValueError:
            print("❗️Wrong answer! Try again.")


# ----------------------------------------- PURCHASE ORDERS ------------------------------------------
def users_purchase_orders(username):
    print(f'''
********** PURCHASE ORDERS ********** 
''')
    if len(purchase_orders) == 0:
        print("You currently have 0 orders.")
    elif len(purchase_orders) != 0:
        print("💳 - PURCHASE ORDERS:")
        for key, value in purchase_orders.items():
            if value.endswith(username):
                print(key, '-', value)
    print()
    print('''1. ACCEPT A TERACODE ORDER
2. DELETE A TERACODE ORDER
3. Exit
''')
    while True:
        menu_button = input("Button: ")
        try:
            if int(menu_button) == 3:
                profile(username)
            if int(menu_button) == 2:
                delete_order = int(input("Which Order would you like to delete? #"))
                purchase_orders.pop(delete_order)
                users_purchase_orders(username)
            if int(menu_button) == 1:
                while True:
                    order_number = int(input("Which Order would you like to accept? #"))
                    if order_number not in purchase_orders:
                        print("❗️This order does not exist! Try again.")
                    else:
                        while True:
                            user = input("Please 'Type' the username of the user who placed the order: ")
                            for key, value in purchase_orders.items():
                                if user not in value:
                                    print("❗️The username doesn't match the purchase order.")
                            else:
                                while True:
                                    teracodes_amount = int(input("How many Teracodes are you willing to sell? 🔸"))
                                    if teracodes_amount > terastacks_accounts[username]:
                                        print("❗️You don't have enough Teracodes to completes the transaction.")
                                    else:
                                        teracode_value = teracodes_amount * teracode_info["teracode_price"]
                                        print()
                                        print(
                                            f'''You will sell {teracodes_amount}🔸 to {user} for a return of ${teracode_value}.''')
                                        print()
                                        while True:
                                            confirm_sale = input("Do you wish to proceed? [Y/N] ")
                                            if confirm_sale.upper() == "N":
                                                users_purchase_orders(username)
                                            if confirm_sale.upper() == "Y":
                                                if fiat_accounts[user] < teracode_value:
                                                    print(
                                                        "❗️The purchase order could not be completed. Try again another time.")
                                                else:
                                                    fiat_accounts[user] -= teracode_value
                                                    fiat_accounts[username] += teracode_value
                                                    terastacks_accounts[user] += teracodes_amount
                                                    terastacks_accounts[username] -= teracodes_amount
                                                    serial_numbers["sale_number"] += 1
                                                    sales[serial_numbers[
                                                        "sale_number"]] = f'''{username} sold {teracodes_amount}🔸 for ${teracode_value} to {user} '''
                                                    serial_numbers["purchase_number"] += 1
                                                    terastacks_purchases[serial_numbers[
                                                        "purchase_number"]] = f'''{user} purchased {teracodes_amount}🔸 for ${teracode_value} from {username} '''
                                                    print()
                                                print(
                                                    f'''The purchase order has been completed! We will notify {user}.''')
                                                purchase_orders.pop(order_number)
                                                users_purchase_orders(username)
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


# ----------------------------------------- PERSONAL HISTORY PAGE ------------------------------------------
def personal_history(username):
    print()
    print('**********  ACCOUNT HISTORY **********')
    print()
    print("➡️ - DEPOSITS:")
    for key, value in deposits.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("⬅️ - WITHDRAWALS:")
    for key, value in withdrawals.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("🔄 - TRANSFERS:")
    for key, value in transfers.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("🔶 - TERASTACKS PURCHASES:")
    for key, value in terastacks_purchases.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("🔶 - MARKET PURCHASES:")
    for key, value in market_purchases.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("🔶 - OTHER USERS PURCHASES:")
    for key, value in user_purchases.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("💰 - TERACODES SALES:")
    for key, value in sales.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("📈 - THE MARKET:")
    for key, value in market.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("🔂 - REFUND DEMANDS:")
    for key, value in refund_demands.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    print("🔂 - REFUNDED:")
    for key, value in refunded.items():
        if value.startswith(username):
            print(key, '-', value)
    print()
    while True:
        leave = input("Type 'LEAVE' to exit: ")
        if leave.upper() == "LEAVE":
            profile(username)
            break
        else:
            print("❗️Wrong answer! Try again")


# ----------------------------------------- SETTINGS MENU ------------------------------------------
def settings(username):
    global block_hash, next_block_hash
    print(f'''
********** SETTINGS ********** 
                
1. MODIFY USERNAME: {username}
2. MODIFY EMAIL: {emails[username]}
3. MODIFY PASSWORD: PRIVATE
4. ID NUMBER: {user_numbers[username]}
5. DELETE ACCOUNT
6. Exit
''')
    while True:
        button = input("Button: ")
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
                        print()
                        print(f'''You successfully changed your username from {username} to {new_username}!''')
                        settings(new_username)
                        break
            if int(button) == 2:
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
                            f'''You successfully changed your email address from {emails[username]} to {new_email}!''')
                        emails[username] = new_email
                        settings(username)
                        break
            if int(button) == 3:
                while True:
                    password = input("Current Password:  ")
                    if password != passwords[username]:
                        print("❗️Wrong Password! Try Again")
                    else:
                        new_password = input("NEW PASSWORD: ")
                        passwords[username] = new_password
                        print()
                        print("You successfully changed your password!")
                        settings(username)
                        break
            if int(button) == 5:
                question = input("❗️Are you sure you wish to permanently delete your account? [Y/N]")
                if question.upper() == "N":
                    settings(username)
                if question.upper() == "Y":
                    fiat_accounts.pop(username)
                    terastacks_accounts.pop(username)
                    emails.pop(username)
                    passwords.pop(username)
                    teracode_info["teracode_price"] -= 1
                    serial_numbers["block_number"] += 1
                    if serial_numbers["block_number"] == 1:
                        block_number = f'''Block {serial_numbers["block_number"]}'''
                        transaction = f'''{user_numbers[username]} deleted his account | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                        block_data = block_number + " | " + transaction
                        block_hash = hashlib.sha256(block_data.encode()).hexdigest()
                        block = f'''{block_data} | {block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                    elif serial_numbers["block_number"] == 2:
                        block_number = f'''Block {serial_numbers["block_number"]}'''
                        transaction = f'''{user_numbers[username]} deleted his account | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                        next_block_data = block_number + " | " + transaction + " | " + block_hash
                        next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                        block = f'''{next_block_data} | {next_block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                    elif serial_numbers["block_number"] > 2:
                        block_number = f'''Block {serial_numbers["block_number"]}'''
                        transaction = f'''{user_numbers[username]} deleted his account | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                        next_block_data = block_number + " | " + transaction + " | " + next_block_hash
                        next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                        block = f'''{next_block_data} | {next_block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                    print("Terastacks is sorry to see you leave.")
                    welcome()
            if int(button) == 6:
                profile(username)
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


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
                purchase_teracodes(username)
                break
            if int(button) == 2:
                sell_teracodes(username)
                break
            if int(button) == 3:
                transfer_teracodes(username)
                break
            if int(button) == 4:
                homepage(username)
                break
            else:
                print("❗️Wrong button. Try again.")
        except ValueError:
            print("❗️Wrong Button. Try again.")


# ----------------------------------------- PURCHASE TERACODES PAGE ------------------------------------------
def purchase_teracodes(username):
    global block_hash, next_block_hash
    print('''
********** BUY TERACODES ********** ''')
    terastacks_balance()
    print()
    if fiat_accounts[username] < teracode_info["teracode_price"]:
        print()
        print("❗️You currently don't have enough FIAT to purchase a Teracode.")
        teracodes(username)
    while True:
        print()
        purchase_amount = int(input("How many Teracodes do you wish to purchase? 🔸"))
        teracode_value = purchase_amount * teracode_info["teracode_price"]
        print()
        while True:
            proceed = input(f'''This transaction will cost you ${teracode_value}. Do you wish to proceed? [Y/N] ''')
            if proceed.upper() == "N":
                teracodes(username)
            if proceed.upper() == "Y":
                if fiat_accounts[username] < teracode_value:
                    print()
                    print(f"❗️You currently don't have enough FIAT to purchase {purchase_amount}🔸.")
                    teracodes(username)
                    break
                else:
                    print()
                    print(f'''Purchase your Teracodes from: 
                    1. Terastacks
                    2. The Market
                    3. Other User''')
                    while True:
                        purchase_from = input("Button: ")
                        try:
                            if int(purchase_from) == 1:
                                while True:
                                    if terastacks_accounts["terastacks"] == 0:
                                        print(
                                            "❗️Unfortunately, Terastacks has no more Teracodes to sell until the next batch is released.")
                                        teracodes(username)
                                    if purchase_amount > terastacks_accounts["terastacks"]:
                                        print(
                                            f'''❗️Unfortunately, Terastacks currently only has {terastacks_accounts["terastacks"]}🔸 to sell.''')
                                        teracodes(username)
                                    else:
                                        terastacks_accounts[username] += purchase_amount
                                        terastacks_accounts["terastacks"] -= purchase_amount
                                        fiat_accounts[username] -= teracode_value
                                        fiat_accounts["terastacks"] += teracode_value
                                        fiat_accounts["terastacks"] -= 1
                                        teracode_info["teracode_price"] += 1
                                        serial_numbers["purchase_number"] += 1
                                        terastacks_purchases[serial_numbers[
                                            "purchase_number"]] = f'''{user_numbers[username]} purchased {purchase_amount}🔸 for ${teracode_value} '''
                                        print(
                                            f'''You successfully purchased {purchase_amount}🔸 for ${teracode_value} from Terastacks!''')
                                        serial_numbers["block_number"] += 1
                                        if serial_numbers["block_number"] == 1:
                                            block_number = f'''Block {serial_numbers["block_number"]}'''
                                            transaction = f'''{user_numbers[username]} purchased {purchase_amount}🔸 for ${teracode_value} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                                            block_data = block_number + " | " + transaction
                                            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
                                            block = f'''{block_data} | {block_hash}'''
                                            serial_numbers["blockchain_sn"] += 1
                                            blockchain[serial_numbers["blockchain_sn"]] = block
                                        elif serial_numbers["block_number"] == 2:
                                            block_number = f'''Block {serial_numbers["block_number"]}'''
                                            transaction = f'''{user_numbers[username]} purchased {purchase_amount}🔸 for ${teracode_value} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                                            next_block_data = block_number + " | " + transaction + " | " + block_hash
                                            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                                            block = f'''{next_block_data} | {next_block_hash}'''
                                            serial_numbers["blockchain_sn"] += 1
                                            blockchain[serial_numbers["blockchain_sn"]] = block
                                        elif serial_numbers["block_number"] > 2:
                                            block_number = f'''Block {serial_numbers["block_number"]}'''
                                            transaction = f'''{user_numbers[username]} purchased {purchase_amount}🔸 for ${teracode_value} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                                            next_block_data = block_number + " | " + transaction + " | " + next_block_hash
                                            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                                            block = f'''{next_block_data} | {next_block_hash}'''
                                            serial_numbers["blockchain_sn"] += 1
                                            blockchain[serial_numbers["blockchain_sn"]] = block
                                        teracodes(username)
                                        break
                            if int(purchase_from) == 2:
                                market_purchase(username)
                            if int(purchase_from) == 3:
                                while True:
                                    print()
                                    user = input("Type the Username you wish to purchase from: ")
                                    if user not in terastacks_accounts:
                                        print("❗️User not found. Try again.")
                                        purchase_teracodes(username)
                                    else:
                                        print()
                                        print(
                                            f'''You placed an order of {purchase_amount}🔸 for ${teracode_value} to {user}.''')
                                        print()
                                        while True:
                                            keep_going = input("Do you wish to send the order? [Y/N] ")
                                            if keep_going.upper() == "N":
                                                teracodes(username)
                                            if keep_going.upper() == "Y":
                                                serial_numbers["purchase_orders_number"] += 1
                                                purchase_orders[serial_numbers[
                                                    "purchase_orders_number"]] = f'''{username} wants to purchase {purchase_amount}🔸 for ${teracode_value} from {user}'''
                                                print()
                                                print(
                                                    f'''You have successfully placed your order! We will notify {user}.''')
                                                teracodes(username)
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
                        except ValueError:
                            print("❗️Wrong button! Try again.")
            else:
                print("❗️Wrong answer! Try again.")


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
                            print(f'You currently have {terastacks_accounts[username]}🔸 to sell.')
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
                                            f'''You want to sell {teracode_amount}🔸 for ${teracode_value} to Terastacks.''')
                                        print()
                                        print(
                                            "* Note that once the offer has been sent, the value of those specific Teracodes will be frozen *")
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
                                                    f'''You have successfully sent your offer! We will notify Terastacks.''')
                                                teracodes(username)
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
                                    if int(button) == 2:
                                        market_sale(username)
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
                                print(f'''You will send {teracodes_amount}🔸 to {teracodes_receiver}.''')
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
                                            f'''You successfully sent {teracodes_amount}🔸 to {teracodes_receiver}!''')
                                        teracodes(username)
                                        break
                                    else:
                                        print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


# ----------------------------------------- MARKET MENU ------------------------------------------
def the_market(username):
    print(f'''
    ********** THE MARKET  ********** ''')
    for key, value in market.items():
        print(key, ':', value)
    print()
    print(f'''
1. BUY TERACODES FROM THE MARKET
2. SELL TERACODES ON THE MARKET
3. Exit
''')
    print()
    while True:
        button = input("Button: ")
        try:
            if int(button) == 1:
                market_purchase(username)
                break
            if int(button) == 2:
                market_sale(username)
                break
            if int(button) == 3:
                homepage(username)
                break
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


# ----------------------------------------- MARKET PURCHASE (function)  ------------------------------------------
def market_purchase(username):
    while True:
        if len(market) == 0:
            print("There are currently no users selling on The Market.")
            teracodes(username)
            break
        else:
            print()
            print(f'''********** THE MARKET  ********** ''')
            for key, value in market.items():
                print(key, ':', value)
            print()
            while True:
                purchase_amount = int(input("How many Teracodes would you like to purchase? 🔸"))
                teracode_value = purchase_amount * teracode_info["teracode_price"]
                if teracode_value > fiat_accounts[username]:
                    print(f"❗️You do not have enough FIAT to purchase {purchase_amount}🔸.")
                print()
                while True:
                    proceed = input(f"This transaction will cost you ${teracode_value}, do you wish to proceed? [Y/N]")
                    if proceed.upper() == "N":
                        market_purchase(username)
                    if proceed.upper() == "Y":
                        while True:
                            buying_from = input("Type the username you want to purchase from: ")
                            if buying_from not in market:
                                print("❗️User not found in The Market. Try again.")
                                the_market(username)
                            if buying_from == username:
                                print("❗️You can't buy from yourself.")
                                market_purchase(username)
                            else:
                                if purchase_amount > market[buying_from]:
                                    print("❗️This user does not have enough Teracodes on The Market.")
                                else:
                                    fiat_accounts[username] -= teracode_value
                                    fiat_accounts[buying_from] += teracode_value
                                    terastacks_accounts[username] += purchase_amount
                                    terastacks_accounts[buying_from] -= purchase_amount
                                    market[buying_from] -= purchase_amount
                                    serial_numbers["purchase_number"] += 1
                                    terastacks_purchases[serial_numbers[
                                        "purchase_number"]] = f"{username} purchased {purchase_amount}🔸 for ${teracode_value} from {buying_from} "
                                    print(
                                        f"You successfully purchased {purchase_amount}🔸 from {buying_from} for ${teracode_value}.")
                                    the_market(username)
                                    break
                    else:
                        print("❗️Wrong answer! Try again.")


# ----------------------------------------- MARKET SALE (function)  ------------------------------------------
def market_sale(username):
    print(f'''
********** THE MARKET  ********** ''')
    for key, value in market.items():
        print(key, ':', value)
    print()
    while True:
        print('''
1. SELL TO THE MARKET
2. Exit 
        ''')
        while True:
            button = input("Button: ")
            try:
                if int(button) == 2:
                    the_market(username)
                if int(button) == 1:
                    account_balance(username)
                    print()
                    teracodes_amount = int(input("How many Teracodes do you wish to place on The Market? 🔸"))
                    if terastacks_accounts[username] < teracodes_amount:
                        print("❗️You don't have enough Teracodes to complete the placement.")
                        market_sale(username)
                    else:
                        teracode_value = teracodes_amount * teracode_info["teracode_price"]
                        print()
                        print(f'''You will place {teracodes_amount}🔸 worth ${teracode_value} on The Market.''')
                        while True:
                            proceed = input("Do you wish to proceed? [Y/N] ")
                            if proceed.upper() == "N":
                                market_purchase(username)
                                break
                            if proceed.upper() == "Y":
                                market[username] = teracodes_amount
                                market_sale(username)
                                break
                            else:
                                print("❗️Wrong answer! Try again.")
                else:
                    print("❗️Wrong button! Try again.")
            except ValueError:
                print("❗️Wrong button! Try again.")


# ----------------------------------------- THE BLOCKCHAIN PAGE ------------------------------------------
def the_blockchain(username):
    print(f'''
    ********** THE BLOCKCHAIN ********** ''')
    print('''
1. VIEW THE CHAIN
2. Exit
''')
    while True:
        button = input("Button: ")
        try:
            if int(button) == 2:
                homepage(username)
            if int(button) == 1:
                print("          BLOCKCHAIN          ")
                for key, value in blockchain.items():
                    print(key, '-', value)
                    print()
                homepage(username)
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


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
5. Log Out
''')
    while True:
        button = input("Button: ")
        try:
            if int(button) == 1:
                terastacks_databases()
                break
            if int(button) == 2:
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
                welcome()
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
    print("💰 - FIAT ACCOUNTS:")
    for key, value in fiat_accounts.items():
        print(key, '-', value)
    print()
    print("🔶 - TERASTACKS ACCOUNTS:")
    for key, value in terastacks_accounts.items():
        print(key, '-', value)
    print()
    print("💳 - STRIPE ACCOUNTS:")
    for key, value in stripe_account.items():
        print(key, '-', value)
    print()
    print("🆔 - USER NUMBERS:")
    for key, value in user_numbers.items():
        print(key, '-', value)
    print()
    print("📧 - EMAILS DATABASE:")
    for key, value in emails.items():
        print(key, '-', value)
    print()
    print("➡️ - DEPOSITS:")
    for key, value in deposits.items():
        print(key, '-', value)
    print()
    print("⬅️ - WITHDRAWALS:")
    for key, value in withdrawals.items():
        print(key, '-', value)
    print()
    print("🔸 - TERACODES PURCHASES:")
    for key, value in terastacks_purchases.items():
        print(key, '-', value)
    print()
    print("🔸 - MARKET PURCHASES:")
    for key, value in market_purchases.items():
        print(key, '-', value)
    print()
    print("🔸 - OTHER USERS PURCHASES:")
    for key, value in user_purchases.items():
        print(key, '-', value)
    print()
    print("💵 - TERACODES SALES:")
    for key, value in sales.items():
        print(key, '-', value)
    print()
    print("📈 - THE MARKET:")
    for key, value in market.items():
        print(key, '-', value)
    print()
    while True:
        leave = input("Type 'LEAVE' to exit: ")
        if leave.upper() == "LEAVE":
            terastacks_backdoor()
            break
        else:
            print("❗️Wrong answer! Try again.")


# ----------------------------------------- TERASTACKS REFUNDS ------------------------------------------
def terastacks_refunds():
    global block_hash, block_hash, next_block_hash
    print(f'''
********** TERASTACKS REFUNDS ********** 
''')
    print("🔂 - REFUND DEMANDS:")
    for key, value in refund_demands.items():
        print(key, '-', value)
    print()
    print("🔂 - REFUNDED:")
    for key, value in refunded.items():
        print(key, '-', value)
    print(f'''
1. REFUND
2. Exit 
''')
    while True:
        proceed = input("Button: ")
        try:
            if int(proceed) == 2:
                terastacks_backdoor()
                break
            if int(proceed) == 1:
                print()
                refund_transaction = input("Which Transaction # would you like to refund? #")
                refund_cost = int(input("How much do you need to refund? $"))
                if refund_cost > fiat_accounts["terastacks"]:
                    print("Terastacks currently doesn't have enough FIAT to refund the transaction.")
                    terastacks_refunds()
                refund_return = int(input("How many Teracodes will you reclaim? 🔸"))
                while True:
                    refund_receiver = input("Enter the username of the refund receiver: ")
                    if refund_receiver not in terastacks_accounts:
                        print("❗️User not found. Try again.")
                    if terastacks_accounts[refund_receiver] < refund_return:
                        print()
                        print("❗️The user doesn't have enough Teracodes to be currently refunded. CONTACT USER!")
                        terastacks_refunds()
                    else:
                        break
                print()
                print(
                    f'''You will refund Transaction #{refund_transaction} - {refund_receiver} ${refund_cost} for {refund_return}🔸.''')
                while True:
                    proceed_2 = input("Do you wish to proceed? [Y/N]")
                    if proceed_2.upper() == "N":
                        terastacks_refunds()
                        break
                    if proceed_2.upper() == "Y":
                        refunded[refund_transaction] = f'''{refund_receiver} - ${refund_cost} for {refund_return}🔸'''
                        fiat_accounts[refund_receiver] += refund_cost
                        fiat_accounts["terastacks"] -= refund_cost
                        terastacks_accounts[refund_receiver] -= refund_return
                        terastacks_accounts["terastacks"] += refund_return
                        teracode_info["teracode_price"] -= 1
                        print()
                        print(
                            f'''️{refund_receiver} received a refund for Transaction #{refund_transaction} - ${refund_cost} for {refund_return}🔸. ''')
                        refund_demands.pop(int(refund_transaction))
                        serial_numbers["block_number"] += 1
                        if serial_numbers["block_number"] == 1:
                            block_number = f'''Block {serial_numbers["block_number"]}'''
                            transaction = f'''Terastacks refunded {refund_receiver} {refund_return}🔸 for ${refund_cost} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                            block_data = block_number + " | " + transaction
                            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
                            block = f'''{block_data} | {block_hash}'''
                            serial_numbers["blockchain_sn"] += 1
                            blockchain[serial_numbers["blockchain_sn"]] = block
                        elif serial_numbers["block_number"] == 2:
                            block_number = f'''Block {serial_numbers["block_number"]}'''
                            transaction = f'''Terastacks refunded {refund_receiver} {refund_return}🔸 for ${refund_cost} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                            next_block_data = block_number + " | " + transaction + " | " + block_hash
                            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                            block = f'''{next_block_data} | {next_block_hash}'''
                            serial_numbers["blockchain_sn"] += 1
                            blockchain[serial_numbers["blockchain_sn"]] = block
                        elif serial_numbers["block_number"] > 2:
                            block_number = f'''Block {serial_numbers["block_number"]}'''
                            transaction = f'''Terastacks refunded {refund_receiver} {refund_return}🔸 for ${refund_cost} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                            next_block_data = block_number + " | " + transaction + " | " + next_block_hash
                            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                            block = f'''{next_block_data} | {next_block_hash}'''
                            serial_numbers["blockchain_sn"] += 1
                            blockchain[serial_numbers["blockchain_sn"]] = block
                        terastacks_refunds()
                        break
                    else:
                        print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


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
                                                    f'''The purchase order has been completed! We will notify {user}.''')
                                                terastacks_inbox.pop(order_number)
                                                tera_inbox_fn()
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RUN THE APPLICATION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
welcome()
