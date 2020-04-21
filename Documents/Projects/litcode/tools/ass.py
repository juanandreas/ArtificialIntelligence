import hashlib
from collections import defaultdict
from random import random

startBalances= [5, 0, 0]
pendingTransactions= [[0,1,5], 
 [1,2,5]]
blockSize= 2

def sha1(text):
    s = hashlib.sha1()
    s.update(text.encode('utf-8'))
    return s.hexdigest()

def get_prevBlockHash():
    
    return "0000000000000000000000000000000000000000"


def get_nonce(prevBlockHash, valid_transactions, length=int(random())):
    """Generate pseudorandom number."""
    block_str = "_____"
    nonce_mem = {}
    while block_str[0:4] != "0000":
        nonce = ''.join([str(random.randint(0, 9)) for i in range(length)])
        if nonce not in nonce_mem:
            print(nonce)
            info = prevBlockHash + ", " + nonce + ", " + valid_transactions
            block_str = sha1(info)
        
        nonce_mem[nonce] = nonce
    
    return nonce


def get_validTransactions(pending):
    d = defaultdict(int)
    
    return "[[0, 1, 5], [1, 2, 5]]"

def getLatestBlock(startBalances, pendingTransactions, blockSize):
    '''
    create a blockchian that includes all valid pending transactions
    in the order in which they are given and return the last block
    
    blocks are encoded as strings of the form:
    ["blockHash" | "prevBlockHash" | "nonce" | "blockTransactions"]
    
    blockchain = immutable linked list of 'blocks' each containing
    up to 5 valid transactions. Each block is linked to the previous
    block via a cryptographic hash rather than a pointer.
    
    startBalances = an array representing starting balances. elem with index i and value x
    initializes the balance of the node with address i to x
    
    pendingTransactions = two-d array of integers, where each subarray is of the form
    [fromAddress, toAddress, value]
    
    blockSize = integer specifying max number of transactions
                that can be included in a block
    '''
    
    # print(sha1("0000000000000000000000000000000000000000, 28427, [[0, 1, 5], [1, 2, 5]]"))
    # print(str(startBalances))
    # print(sha1("0000"))
    
    prevBlockHash = get_prevBlockHash()
    valid_transactions = get_validTransactions(pendingTransactions)

    nonce = get_nonce(prevBlockHash, valid_transactions)
    
    info = prevBlockHash + ", " + nonce + ", " + valid_transactions
    
    latestBlockHash = sha1(info)
    
    res = latestBlockHash + ", " + info
    
    return res

getLatestBlock(startBalances, pendingTransactions, blockSize)
