#!/usr/bin/env python3
#Time-stamp: <Tue Oct 09 22:34:58 JST 2018 hamada>
'''
Example: an analysys of the top miners
'''

import web3
import sys

def puts_block(block):
    for key in block:
        print (key, block[key])

if __name__ == "__main__":
    #provider = web3.HTTPProvider('http://117.102.189.70:28545') # secondary provider
    provider = web3.HTTPProvider('http://117.102.189.70:18545') # first provider
    www3 = web3.Web3(provider)

    if True:

        block_latest = www3.eth.getBlock('latest')
        #puts_block(block_latest)
        bnum_latest =block_latest['number']
        print ("current block#:", bnum_latest)

        miner_count = {}

        for i in range(1000):
            bnum = bnum_latest - i
            block = www3.eth.getBlock(bnum)
            try:
                miner = block['miner'].lower()
                if miner not in miner_count:
                    miner_count[miner] = 1
                else:
                    miner_count[miner] += 1
            except:
                print(sys.exc_info())

            print (bnum, miner, miner_count[miner])

        miner_list = sorted(miner_count.items(), key=lambda x: -x[1])
        for k, v in miner_list:
            print (k, v)
