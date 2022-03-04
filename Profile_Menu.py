from Dictionaries import account_balance

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
                import FIAT_Actions
                FIAT_Actions.deposits_fn(username)
            if int(button) == 2:
                import FIAT_Actions
                FIAT_Actions.withdrawals_fn(username)
            if int(button) == 3:
                import FIAT_Actions
                FIAT_Actions.transfer(username)
            if int(button) == 4:
                import Refunds
                Refunds.refund_fn(username)
            if int(button) == 5:
                import Purchase_Orders
                Purchase_Orders.users_purchase_orders(username)
            if int(button) == 6:
                import User_History
                User_History.personal_history(username)
            if int(button) == 7:
                import Setting_Menu
                Setting_Menu.settings(username)
            if int(button) == 8:
                import Homepage_Menu
                Homepage_Menu.homepage(username)
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")
