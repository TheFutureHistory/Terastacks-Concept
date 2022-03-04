from Dictionaries import fiat_accounts, terastacks_accounts, emails, passwords, teracode_info, serial_numbers, \
    user_numbers, blockchain, terastacks_balance, terastacks_purchases, purchase_orders, refund_demands, refunded, stripe_account
import hashlib
import datetime
from TERACODES_Actions import teracodes


# ----------------------------------------- DELETE ACCOUNT ------------------------------------------
def delete_account(username):
    global block_hash, next_block_hash
    print("❕Note that if you delete your account, you won't be able to get it back❕")
    question = input("❗️Are you sure you wish to permanently delete your account? [Y/N]")
    if question.upper() == "N":
        import Setting_Menu
        Setting_Menu.settings(username)
    if question.upper() == "Y":
        fiat_accounts.pop(username)
        terastacks_accounts.pop(username)
        emails.pop(username)
        passwords.pop(username)
        teracode_info["teracode_price"] -= 1
        serial_numbers["block_number"] += 1
        if serial_numbers["block_number"] == 1:
            block_number = f'''Block {serial_numbers["block_number"]}'''
            transaction = f'''{username} deleted his account | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
            block_data = block_number + " | " + transaction
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            block = f'''{block_data} | {block_hash}'''
            serial_numbers["blockchain_sn"] += 1
            blockchain[serial_numbers["blockchain_sn"]] = block
        elif serial_numbers["block_number"] == 2:
            block_number = f'''Block {serial_numbers["block_number"]}'''
            transaction = f'''{username} deleted his account | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
            next_block_data = block_number + " | " + transaction + " | " + block_hash
            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
            block = f'''{next_block_data} | {next_block_hash}'''
            serial_numbers["blockchain_sn"] += 1
            blockchain[serial_numbers["blockchain_sn"]] = block
        elif serial_numbers["block_number"] > 2:
            block_number = f'''Block {serial_numbers["block_number"]}'''
            transaction = f'''{username} deleted his account | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
            next_block_data = block_number + " | " + transaction + " | " + next_block_hash
            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
            block = f'''{next_block_data} | {next_block_hash}'''
            serial_numbers["blockchain_sn"] += 1
            blockchain[serial_numbers["blockchain_sn"]] = block
        print("✅ Account permanently deleted! Terastacks is sorry to see you leave.")
        import WelcomeMod
        WelcomeMod.welcome()


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
            print(f'''❕ This transaction will cost you ${teracode_value}. ''')
            print()
            proceed = input('Do you wish to proceed? [Y/N] ')
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
                                        stripe_account["terastacks"] -= teracode_value
                                        fiat_accounts["terastacks"] -= 1
                                        teracode_info["teracode_price"] += 1
                                        serial_numbers["purchase_number"] += 1
                                        terastacks_purchases[serial_numbers[
                                            "purchase_number"]] = f'''{username} purchased {purchase_amount}🔸 for ${teracode_value} | {datetime.datetime.now()} '''
                                        print(
                                            f'''✅ You successfully purchased {purchase_amount}🔸 for ${teracode_value} from Terastacks!''')
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
                                import MARKET_Actions
                                MARKET_Actions.market_purchase(username)
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
                                            f'''❕ You placed an order of {purchase_amount}🔸 for ${teracode_value} to {user}.''')
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
                                                    f'''✅ You have successfully placed your order! We will notify {user}.''')
                                                teracodes(username)
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
                        except ValueError:
                            print("❗️Wrong button! Try again.")
            else:
                print("❗️Wrong answer! Try again.")


# ----------------------------------------- TERASTACKS REFUNDS ------------------------------------------
def terastacks_refunds():
    global block_hash, next_block_hash
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
                from Terastacks_Backdoor import terastacks_backdoor
                terastacks_backdoor()
                break
            if int(proceed) == 1:
                print()
                refund_transaction = input("Which Transaction # would you like to refund? #")
                refund_cost = int(input("How much do you need to refund? $"))
                if refund_cost > fiat_accounts["terastacks"]:
                    print("❗️ Terastacks currently doesn't have enough FIAT to refund the transaction.")
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
                    f'''❕ You will refund Transaction #{refund_transaction} - {refund_receiver} ${refund_cost} for {refund_return}🔸.''')
                while True:
                    proceed_2 = input("Do you wish to proceed? [Y/N]")
                    if proceed_2.upper() == "N":
                        terastacks_refunds()
                        break
                    if proceed_2.upper() == "Y":
                        refunded[refund_transaction] = f'''{refund_receiver} - ${refund_cost} for {refund_return}🔸 | {datetime.datetime.now()}'''
                        fiat_accounts[refund_receiver] += refund_cost
                        fiat_accounts["terastacks"] -= refund_cost
                        terastacks_accounts[refund_receiver] -= refund_return
                        terastacks_accounts["terastacks"] += refund_return
                        teracode_info["teracode_price"] -= 1
                        print()
                        print(
                            f'''✅️{refund_receiver} received a refund for Transaction #{refund_transaction} - ${refund_cost} for {refund_return}🔸. ''')

                        refund_demands.pop(int(refund_transaction))
                        serial_numbers["block_number"] += 1
                        if serial_numbers["block_number"] == 1:
                            block_number = f'''Block {serial_numbers["block_number"]}'''
                            transaction = f'''Terastacks refunded {user_numbers[refund_receiver]} {refund_return}🔸 for ${refund_cost} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                            block_data = block_number + " | " + transaction
                            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
                            block = f'''{block_data} | {block_hash}'''
                            serial_numbers["blockchain_sn"] += 1
                            blockchain[serial_numbers["blockchain_sn"]] = block
                        elif serial_numbers["block_number"] == 2:
                            block_number = f'''Block {serial_numbers["block_number"]}'''
                            transaction = f'''Terastacks refunded {user_numbers[refund_receiver]} {refund_return}🔸 for ${refund_cost} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
                            next_block_data = block_number + " | " + transaction + " | " + block_hash
                            next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                            block = f'''{next_block_data} | {next_block_hash}'''
                            serial_numbers["blockchain_sn"] += 1
                            blockchain[serial_numbers["blockchain_sn"]] = block
                        elif serial_numbers["block_number"] > 2:
                            block_number = f'''Block {serial_numbers["block_number"]}'''
                            transaction = f'''Terastacks refunded {user_numbers[refund_receiver]} {refund_return}🔸 for ${refund_cost} | {datetime.datetime.now()} | Teracodes left: {terastacks_accounts["terastacks"]}🔸 | New Price: ${teracode_info["teracode_price"]} each '''
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
