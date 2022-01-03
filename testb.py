# A hash module/library to create one way encrypted messages
import hashlib


# Class for the loaner
class Loaner:
    def __init__(self, fname, lname, l_id):
        self.fname = fname
        self.lname = lname
        self.l_id = l_id

    def loaner_info(self):
        print("Loaner Information:")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Loaner ID: {self.l_id}")

    # A method to search for a registerd loaner via the ID
    def checkloaner(self, cid):
        if cid == self.l_id:
            return True
        else:
            return False


# A class to define a client
class Client:
    def __init__(self, fname: str, lname: str, c_id):
        self.fname = fname
        self.lname = lname
        self.c_id = c_id

    def client_info(self):
        print("Client Information:")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Client ID: {self.c_id}")

    # A method to search for the client via the ID
    def checkclient(self, pid):
        if pid == self.c_id:
            return True
        else:
            return False


# ==========================================================
class Transaction:
    def __init__(
        self, amount, lon_id=None, cl_id=None, t_id=None, t_hash=None, prev_hash=None
    ):
        self.amount = amount
        self.lon_id = lon_id
        self.cl_id = cl_id
        self.t_id = t_id
        self.prev_hash = prev_hash
        self.t_hash = t_hash
        # self.previous_block_hash = previous_block_hash

        # self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        # self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def transaction_info(self):
        print("Transaction Details:")
        print(f"IDs: {self.lon_id} {self.cl_id} {self.t_id}")
        print(f"Amount of Money: {self.amount}")
        print(f"Block Hash: {self.t_hash}")
        print(f"Previous Block Hash: {self.prev_hash}")

    def checktransaction(self, tid):
        if tid == self.t_id:
            return True
        else:
            return False

    # class MMBlockCoin:
    #     def __init__(self, previous_block_hash, transaction_list):

    #         self.previous_block_hash = previous_block_hash
    #         self.transaction_list = transaction_list


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_first_block()

    def print_blocks(self):
        strings = []
        for transaction in self.chain:
            transaction.transaction_info()

    def generate_first_block(self):
        self.chain.append(Transaction("0", ["First Block"]))

    def create_block_from_transaction(self, lon_id, cl_id, t_id, amount):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(Transaction(amount, lon_id, cl_id, t_id))

    def createblock(self, transaction):
        transaction.previous_block_hash = self.last_block.block_hash
        self.chain.append(transaction)

    def display_chain(self):
        for i in range(len(self.chain)):
            self.chain[i].transaction_info()
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]


# ==========================================================
# Various lists to store the loaner, client, and transaction data
loaners = []
clients = []
transactions = [Transaction("0", ["First Block"], t_hash="0")]
trblockchain = Blockchain()
# ==========================================================
def menu():
    print("[0] EXIT")
    print("[1] Enter Loaner Information")
    print("[2] Search for Loaner")
    print("[3] Enter Client Information")
    print("[4] Search for Client")
    print("[5] Create a Transaction")
    print("[6] Display Transaction Chain")
    print("[7] Finalize Transaction")


# ==========================================================
menu()
option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        for i in range(3):
            loaner_fname = input("fname:")
            loaner_lname = input("lname:")
            loaner_id = input("id:")
            loaners.append(Loaner(loaner_fname, loaner_lname, loaner_id))
    elif option == 2:
        loanerid_forsearch = input("PLEASE ENTER YOUR Loaner's ID:")
        for lonr in loaners:
            if lonr.checkloaner(loanerid_forsearch):
                lonr.loaner_info()
    elif option == 3:
        for i in range(3):
            cli_fname = input("fname:")
            cli_lname = input("lname:")
            cli_id = input("id:")
            clients.append(Client(cli_fname, cli_lname, cli_id))
    elif option == 4:
        cliid_forsearch = input("PLEASE ENTER YOUR Client's ID:")
        for cl in clients:
            if cl.checkclient(cliid_forsearch):
                cl.client_info()
    elif option == 5:
        for i in range(3):
            lon_id = input("Please Enter Loaner ID:")
            cl_id = input("Please Enter Client ID:")
            t_id = input("Please Enter a ID for the Transaction:")
            amount = input("Enter The Amount of Money to be Loaned:")
            t_hash = hashlib.sha256(str([lon_id, cl_id, t_id, amount]).encode()).hexdigest()
            prev_hash = transactions[-1].t_hash
            transactions.append(Transaction(amount, lon_id, cl_id, t_id, t_hash, prev_hash))
    elif option == 6:
        for trans in transactions:
            trans.transaction_info()
    elif option == 7:
        loanerid_forsearch = input("PLEASE ENTER YOUR Loaner's ID:")
        for lonr in loaners:
            if lonr.checkloaner(loanerid_forsearch):
                lonr.loaner_info()
        cliid_forsearch = input("PLEASE ENTER YOUR Client's ID:")
        for cli in clients:
            if cli.checkclient(cliid_forsearch):
                cli.client_info()
        transactionid_forsearch = input("Please Enter Transaction ID:")
        for taction in transactions:
            if taction.checktransaction(transactionid_forsearch):
                taction.transaction_info()
                trblockchain.createblock(taction)
        trblockchain.display_chain()
    else:
        print("Invalid")
    print()
    menu()
    option = int(input("Enter your option:"))
