#!/usr/bin/env python3
import web3

if __name__ == "__main__":

    provider = web3.HTTPProvider('http://192.168.1.2:18545') # ropsten node
    www3 = web3.Web3(provider)

    wei = www3.eth.getBalance("0x81b7E08F65Bdf5648606c89998A9CC8164397647")
    eth = www3.fromWei(wei, "ether")
    bnum = www3.eth.blockNumber
    print(bnum, wei, eth)

    print ('####################')
    print ('# Looking up blocks ')

    if True:
        print ('# get a block by number')
        block0 = www3.eth.getBlock(777777)
        print (block0)

        print ("# get a block by it's hash")
        block1 = www3.eth.getBlock('0xba69bebfc9f48bb6d176a5eff0414b4705ad1344af5d12cbade59d7973fd2281')
        print (block1)

        assert(block0 == block1)

