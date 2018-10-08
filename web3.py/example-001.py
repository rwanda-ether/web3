#!/usr/bin/env python3
import web3

if __name__ == "__main__":

    provider = web3.HTTPProvider('http://192.168.103.200:18545') # ropsten node
    www3 = web3.Web3(provider)

    wei = www3.eth.getBalance("0x81b7E08F65Bdf5648606c89998A9CC8164397647")
    eth = www3.fromWei(wei, "ether")
    bnum = www3.eth.blockNumber
    print(bnum, wei, eth)



