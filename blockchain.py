import hashlib

class MMBlockCoin:
    
    def __init__(self, previous_block_hash, transaction):

        self.previous_block_hash = previous_block_hash
        self.transaction = transaction

        self.block_data = f"{' - '.join(transaction)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(MMBlockCoin("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction):
        previous_block_hash = self.final_block.block_hash
        self.chain.append(MMBlockCoin(previous_block_hash, transaction))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def final_block(self):
        return self.chain[-1]

t1 = "Maher sends 3 MMC to Joe"
t2 = "Joe sends 2.9 MMC to Adam"
t3 = "Adam sends 1.7 MMC to Ahmed"
t4 = "Ahmed sends 0.2 MMC to Yehia"
t5 = "Yehia sends 4.1 MMC to Bery"
t6 = "Bery sends 1.1 MMC to Mohamed"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()