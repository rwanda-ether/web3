#!/usr/bin/env python3
#Time-stamp: <Wed Oct 10 00:44:37 JST 2018 hamada>
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
    #provider = web3.HTTPProvider('http://117.102.189.70:18545') # primary provider
    #provider = web3.HTTPProvider('http://192.168.103.200:18545') # private
    #provider = web3.HTTPProvider('http://192.168.103.201:28545') # private
    provider = web3.HTTPProvider('http://192.168.103.202:18545') # private
    www3 = web3.Web3(provider)

    if True:

        block_latest = www3.eth.getBlock('latest')
        #puts_block(block_latest)
        bnum_latest =block_latest['number']
        print ("current block#:", bnum_latest)

        miner_count = {}

        nblock = 30000
        for i in range(nblock):
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
        print ()
        print ("-------------------------------------------")
        print (" %d miners exist in the last %d blocks." % (len(miner_list), nblock))
        print ("-------------------------------------------")
        print ()
        for k, v in miner_list:
            ratio = v / (nblock * 1.) 
            print ("%s, %d, (%s)" %(k, v, '{:.2%}'.format(ratio)))
