from Dictionaries import deposits, withdrawals, transfers, terastacks_purchases, market_purchases, user_purchases, \
    sales, market, refund_demands, refunded
from Profile_Menu import profile


# ----------------------------------------- USER HISTORY PAGE ------------------------------------------
def personal_history(username):
    print()
    print('**********  ACCOUNT HISTORY **********')
    while True:
        print(f'''
        1. DEPOSITS
        2. WITHDRAWALS
        3. TRANSFERS
        4. TERASTACKS PURCHASES
        5. MARKET PURCHASES
        6. OTHER USE PURCHASES
        7. TERACODES SALES
        8. THE MARKET
        9. REFUND DEMANDS
        10. REFUNDED
        11. Exit''')
        open_fn = input("Open #")
        try:
            if int(open_fn) == 1:
                print()
                print("➡️ - DEPOSITS:")
                for key, value in deposits.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 2:
                print()
                print("⬅️ - WITHDRAWALS:")
                for key, value in withdrawals.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 3:
                print()
                print("🔄 - TRANSFERS:")
                for key, value in transfers.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 4:
                print()
                print("🔶 - TERASTACKS PURCHASES:")
                for key, value in terastacks_purchases.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 5:
                print()
                print("🔶 - MARKET PURCHASES:")
                for key, value in market_purchases.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 6:
                print()
                print("🔶 - OTHER USERS PURCHASES:")
                for key, value in user_purchases.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 7:
                print()
                print("💰 - TERACODES SALES:")
                for key, value in sales.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 8:
                print()
                print("📈 - THE MARKET:")
                for key, value in market.items():
                    if key.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 9:
                print()
                print("🔂 - REFUND DEMANDS:")
                for key, value in refund_demands.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 10:
                print()
                print("🔂 - REFUNDED:")
                for key, value in refunded.items():
                    if value.startswith(username):
                        print(key, '-', value)
            elif int(open_fn) == 11:
                profile(username)
                break
            else:
                print("❗️ Wrong number! Try again.")
        except ValueError:
            print("❗️ Wrong answer! Try again.")





