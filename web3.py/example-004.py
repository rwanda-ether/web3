#!/usr/bin/env python3
#encoding: utf-8
#Time-stamp: <Fri Oct 12 15:13:28 JST 2018 hamada>
#Reference: https://web3py.readthedocs.io/en/stable/overview.html#overview-type-conversions

import web3

'''
Base API
'''

if __name__ == "__main__":

    geth_node = 'http://192.168.103.200:18545' # ropsten node, private
    geth_node = 'http://117.102.189.70:18545'  # ropsten node, public primary
    geth_node = 'http://117.102.189.70:28545'  # ropsten node, public secondary
    geth_node = 'http://254.254.254.254:28545' # not exsisted

    provider = web3.HTTPProvider(geth_node)

    www3 = web3.Web3(provider)

    print (web3.Web3.toHex(0))               # '0x0'
    print (web3.Web3.toHex(1))               # '0x1'
    print (web3.Web3.toHex(0x0))             # '0x0'
    print (web3.Web3.toHex(0x000F))          # '0xf'
    print (web3.Web3.toHex(b''))             # '0x'
    print (web3.Web3.toHex(b'\x00\x0F'))     # '0x000f'
    print (web3.Web3.toHex(False))           # '0x0'
    print (web3.Web3.toHex(True))            # '0x1'
    print (web3.Web3.toHex(hexstr='0x000F')) # '0x000f'
    print (web3.Web3.toHex(hexstr='000F'))   # '0x000f'
    print (web3.Web3.toHex(text=''))         # '0x'
    print (web3.Web3.toHex(text='cowmö'))    # '0x636f776dc3b6'
    print (web3.Web3.toHex(text='Welcome to the Rwanda Ether!!')) # 0x57656c636f6d6520746f20746865205277616e64612045746865722121

