import sys
import csv
sys.path.append('..')
from blockchain_parser.blockchain import Blockchain

# Instantiate the Blockchain by giving the path to the directory
# containing the .blk files created by bitcoind
blockchain = Blockchain(sys.argv[1])
targetCSV = 'out.csv'
table = []
counter = 0

for block in blockchain.get_unordered_blocks():
    if(counter > 200000):
        break
    else:
        for tx in block.transactions:
            for no, output in enumerate(tx.outputs):
                # print("date=%s tx=%s value=%s" % (block.header.timestamp, tx.hash, output.value))
                value = (block.header.timestamp, tx.hash, output.value)
                print (value)
                table.append(value)
        counter+=1
        print(counter)

with open(targetCSV, 'w', newline='\n') as t:
    writer = csv.writer(t)
    writer.writerows(table)
