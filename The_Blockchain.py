from Homepage_Menu import homepage
from Dictionaries import blockchain


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
