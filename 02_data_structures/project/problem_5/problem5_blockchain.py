'''
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created,
and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.
'''


'''
We can break the blockchain down into three main parts.

First is the information hash:
We do this for the information we want to store in the block chain such as transaction time,
data, and information like the previous chain.
'''
import hashlib
import time


'''
The next main component is the block on the blockchain:
Below is an example of attributes you could find in a Block class.
'''
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None


    def calc_hash(self,data):
          sha = hashlib.sha256()

          #hash_str = "We are going to encode this string of data!".encode('utf-8')
          hash_str = data.encode('utf-8')

          sha.update(hash_str)

          return sha.hexdigest()

class BlockChiain:
    def __init__(self):
        self.head = None
        self.curnode = None
        self.elements  = 0

    def insert(self,data):

        if data == None or len(data)==0:
            print('No input data')
            return

        timestamp = time.asctime()
        #print(timestamp)

        #for the first block in this chain
        if self.head == None:
            self.head = Block(timestamp,data,'0')
            self.curnode = self.head
            self.elements+=1
            return
        else:#we already have one block exist
            pre_hash= self.head.hash
            #print(pre_hash)
            newblock = Block(timestamp,data,pre_hash)
            self.curnode.next = newblock
            self.curnode = newblock
            self.elements+=1

    def print_all_chain(self):

        if self.head == None:
            return
        tmp= self.head
        rst = ''
        while tmp!=None:
            rst = rst + '[ '+ tmp.timestamp + ',' + tmp.data +',' + tmp.previous_hash +','+ tmp.hash+']'
            tmp = tmp.next
        print(rst)


'''
Finally you need to link all of this together in a block chain,
which you will be doing by implementing it in a linked list.
All of this will help you build up to a simple but full blockchain implementation!
'''

blackchain = BlockChiain()
blackchain.insert('test')
time.sleep(1)#for different timestamp
blackchain.print_all_chain()
#output: [ Tue May 14 16:27:12 2019,test,0,9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08]
blackchain.insert('test2')
blackchain.print_all_chain()
#output: [ Tue May 14 16:27:12 2019,test,0,9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08][ Tue May 14 16:27:13 2019,test2,9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08,60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752]
time.sleep(2)
blackchain.insert('apple')
blackchain.print_all_chain()
#output: [ Tue May 14 16:27:12 2019,test,0,9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08][ Tue May 14 16:27:13 2019,test2,9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08,60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752][ Tue May 14 16:27:15 2019,apple,9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08,3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b]

print(blackchain.elements)
#output:3

#
