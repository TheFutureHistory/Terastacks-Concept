from Dictionaries import market, teracode_info, fiat_accounts, terastacks_accounts, serial_numbers, \
    terastacks_purchases, account_balance
from Homepage_Menu import homepage
from TERACODES_Actions import teracodes
import datetime


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
            print("❗️ There are currently no users selling on The Market.")
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
                    print(f'''❕This transaction will cost you ${teracode_value}.''')
                    print()
                    proceed = input(f"Do you wish to proceed? [Y/N]")
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
                                        "purchase_number"]] = f"{username} purchased {purchase_amount}🔸 for ${teracode_value} from {buying_from} | {datetime.datetime.now()} "
                                    print(
                                        f"✅ You successfully purchased {purchase_amount}🔸 from {buying_from} for ${teracode_value}.")
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
                        print(f'''❕ You will place {teracodes_amount}🔸 worth ${teracode_value} on The Market.''')
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
