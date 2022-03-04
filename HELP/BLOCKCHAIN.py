import hashlib
import pprint

# Name of block
# Transaction
# Original Block_Hash
# Previous Block Hash

teracode_info = {
    "teracode_price": 1
}

serial_numbers = {
    "transaction_amount": 0,
    "blockchain_sn": 0
}

blockchain = {}


def read_blockchain():
    print("          BLOCKCHAIN          ")
    for key, value in blockchain.items():
        print(key, '-', value)
        print()



def purchase():
    while teracode_info["teracode_price"] < 5:
        username = input("Who buys the Teracodes? ")
        purchase_amount = int(input("How many Teracodes? "))
        teracode_value = purchase_amount * teracode_info["teracode_price"]
        teracode_info["teracode_price"] += 1
        serial_numbers["transaction_amount"] += 1
        transaction_number = f'''Block {serial_numbers["transaction_amount"]}'''
        transaction = f'''{username} purchased {purchase_amount}🔸 for ${teracode_value} from Terastacks'''
        block_data = transaction_number + " - " + transaction
        block_hash = hashlib.sha256(block_data.encode()).hexdigest()
        block = f'''{block_data} | {block_hash}'''
        serial_numbers["blockchain_sn"] += 1
        blockchain[serial_numbers["blockchain_sn"]] = block
        print()
        print(block_data + " | " + block_hash)
        print()
        next = input("What do you want to do next? [EXIT OR CONTINUE]")
        while teracode_info["teracode_price"] < 5:
            if next.upper() == "E":
                read_blockchain()
                break
            if next.upper() == "C":
                username = input("Who buys the Teracodes? ")
                purchase_amount = int(input("How many Teracodes? "))
                teracode_value = purchase_amount * teracode_info["teracode_price"]
                teracode_info["teracode_price"] += 1
                serial_numbers["transaction_amount"] += 1
                transaction_number = f'''Block {serial_numbers["transaction_amount"]}'''
                transaction = f'''{username} purchased {purchase_amount}🔸 for ${teracode_value} from Terastacks'''
                next_block_data = transaction_number + " - " + transaction + " | " + block_hash
                next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                block = f'''{next_block_data} | {next_block_hash}'''
                serial_numbers["blockchain_sn"] += 1
                blockchain[serial_numbers["blockchain_sn"]] = block
                print()
                print(next_block_data + " | " + next_block_hash)
                print()
                next = input("What do you want to do next? [EXIT OR CONTINUE]")
                while teracode_info["teracode_price"] < 5:
                    if next.upper() == "E":
                        read_blockchain()
                        break
                    if next.upper() == "C":
                        username = input("Who buys the Teracodes? ")
                        purchase_amount = int(input("How many Teracodes? "))
                        teracode_value = purchase_amount * teracode_info["teracode_price"]
                        teracode_info["teracode_price"] += 1
                        serial_numbers["transaction_amount"] += 1
                        transaction_number = f'''Block {serial_numbers["transaction_amount"]}'''
                        transaction = f'''{username} purchased {purchase_amount}🔸 for ${teracode_value} from Terastacks'''
                        next_block_data = transaction_number + " - " + transaction + " | " + next_block_hash
                        next_block_hash = hashlib.sha256(next_block_data.encode()).hexdigest()
                        block = f'''{next_block_data} | {next_block_hash}'''
                        serial_numbers["blockchain_sn"] += 1
                        blockchain[serial_numbers["blockchain_sn"]] = block
                        print()
                        print(next_block_data + " | " + next_block_hash)
                        print()
                        next = input("What do you want to do next? [EXIT OR CONTINUE]")



purchase()


# ----------------------------------------------- ORIGINAL BLOCKCHAIN CODE ----------------------------------------

# class TeracodeBlock:

# def __init__(self, previous_block_hash, transaction_list):
# self.previous_block_hash = previous_block_hash
# self.transaction_list = transaction_list

# self.block_data = " - ".join(transaction_list) + " - " + previous_block_hash
# self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


# initial_block = TeracodeBlock("Initial Block", [transaction])
# second_block = TeracodeBlock(initial_block.block_hash, [transaction])
# third_block = TeracodeBlock(second_block.block_hash, [transaction])


# print(initial_block.block_data)
# print(initial_block.block_hash)
# print()
# print(second_block.block_data)
# print(second_block.block_hash)
# print()
# print(third_block.block_data)
# print(third_block.block_hash)
