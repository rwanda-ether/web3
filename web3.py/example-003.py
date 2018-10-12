#!/usr/bin/env python3
#Time-stamp: <Fri Oct 12 15:50:41 JST 2018 hamada>
'''
Example: an analysys of the top miners
'''

import web3
import sys

def puts_block(block):
    for key in block:
        print (key, block[key])

if __name__ == "__main__":
    geth_node = 'http://117.102.189.70:18545'  # ropsten node, public primary
    geth_node = 'http://192.168.103.200:18545' # ropsten node, private
    geth_node = 'http://117.102.189.70:28545'  # ropsten node, public secondary
    geth_node = 'http://192.168.103.201:28545' # ropsten node, private

    provider = web3.HTTPProvider(geth_node)
    www3 = web3.Web3(provider)

    try:
        is_syncing = www3.eth.syncing
        if is_syncing:
            print("Chain hasn't been synced yet.") 
    except:
        print(sys.exc_info())
        print('provider_node:', geth_node)
        exit(-1)

    if True:

        block_latest = www3.eth.getBlock('latest')
        #puts_block(block_latest)
        bnum_latest =block_latest['number']
        print ("current block#:", bnum_latest)

        miner_count = {}

        nblock = 500000
        t_next = block_latest['timestamp']

        for i in range(nblock):
            bnum = bnum_latest - i - 1
            block = www3.eth.getBlock(bnum)
            try:
                miner = block['miner'].lower()
                if miner not in miner_count:
                    miner_count[miner] = 1
                else:
                    miner_count[miner] += 1
            except:
                print(sys.exc_info())

            t_curr = block['timestamp']
            print (bnum, "% 4d"%(t_next-t_curr), miner, miner_count[miner])
            t_next = t_curr

        miner_list = sorted(miner_count.items(), key=lambda x: -x[1])
        print ()
        print ("-------------------------------------------")
        print (" %d miners exist in the last %d blocks." % (len(miner_list), nblock))
        print ("-------------------------------------------")
        print ()
        for k, v in miner_list:
            ratio = v / (nblock * 1.) 
            print ("%s, %d, (%s)" %(k, v, '{:.2%}'.format(ratio)))
