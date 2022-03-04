from Dictionaries import purchase_orders, terastacks_accounts, fiat_accounts, teracode_info, serial_numbers, sales, \
    terastacks_purchases
from Profile_Menu import profile
import datetime


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
                                            f'''❕ You will sell {teracodes_amount}🔸 to {user} for a return of ${teracode_value}.''')
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
                                                        "sale_number"]] = f'''{username} sold {teracodes_amount}🔸 for ${teracode_value} to {user} | {datetime.datetime.now()} '''
                                                    serial_numbers["purchase_number"] += 1
                                                    terastacks_purchases[serial_numbers[
                                                        "purchase_number"]] = f'''{user} purchased {teracodes_amount}🔸 for ${teracode_value} from {username} | {datetime.datetime.now()} '''
                                                    print()
                                                print(
                                                    f'''✅ The purchase order has been completed! We will notify {user}.''')
                                                purchase_orders.pop(order_number)
                                                users_purchase_orders(username)
                                                break
                                            else:
                                                print("❗️Wrong answer! Try again.")
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")
