from Profile_Menu import profile
from Dictionaries import refunded, terastacks_purchases, refund_demands


# ----------------------------------------- REFUND PAGE ------------------------------------------
def refund_fn(username):
    print('''
**********  REFUNDS **********
''')
    print(f'''❕Note that only purchases bought from Terastacks Vault can be refunded❕  
❕Note that any refund will decrease the Teracode's value by $1❕
❕Note that you will be refunded at same purchasing price❕
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
                    print(f'''❕ You wish to be refunded the Transaction #{transaction_number}: {transaction_demand}''')
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
                            f"✅ Your refund demand for Transaction #{transaction_number} has been sent to Terastacks.")
                        refund_fn(username)
                        break
                    else:
                        print("❗️Wrong Answer! Try again.")
            else:
                print("❗️Wrong Number! Try again.")
        except ValueError:
            print("❗️Wrong answer! Try again.")
