from Dictionaries import terastacks_balance


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
                import Profile_Menu
                Profile_Menu.profile(username)
            if int(button) == 2:
                import TERACODES_Actions
                TERACODES_Actions.teracodes(username)
            if int(button) == 3:
                import MARKET_Actions
                MARKET_Actions.the_market(username)
            if int(button) == 4:
                import The_Blockchain
                The_Blockchain.the_blockchain(username)
            if int(button) == 5:
                import WelcomeMod
                WelcomeMod.welcome()
            else:
                print("❗️Wrong button! Try again.")
        except ValueError:
            print("❗️Wrong button! Try again.")
