#!/usr/bin/env python3
# Reference: https://web3py.readthedocs.io/en/stable/examples.html

import web3

if __name__ == "__main__":

    provider = web3.HTTPProvider('http://192.168.103.200:18545') # ropsten node
    www3 = web3.Web3(provider)

    '''
    # Looking up blocks

    Blocks can be looked up by either their number or hash using the
    web3.eth.getBlock API. Block hashes should be in their hexadecimal
    representation. Block numbers
    '''
    if True:
        # get a block by number
        block0 = www3.eth.getBlock(777777)
        print (block0)

        # get a block by it's hash
        block1 = www3.eth.getBlock('0xba69bebfc9f48bb6d176a5eff0414b4705ad1344af5d12cbade59d7973fd2281')
        print (block1)

        assert(block0 == block1)

    '''
    # Getting the latest block
    '''
    if True:

        '''You can also retrieve the latest block using the string 'latest'
        in the web3.eth.getBlock API. '''

        block_latest = www3.eth.getBlock('latest')
        print (block_latest)

        '''If you want to know the latest block number you can use the
        web3.eth.blockNumber property.'''

        print (www3.eth.blockNumber)


    '''
    # Currency conversions

    Web3 can help you convert between denominations. The following
    denominations are supported.

    denomination     amount in wei
    wei                1
    kwei               1000
    babbage            1000
    femtoether         1000
    mwei               1000000
    lovelace           1000000
    picoether          1000000
    gwei               1000000000
    shannon            1000000000
    nanoether          1000000000
    nano               1000000000
    szabo              1000000000000
    microether         1000000000000
    micro              1000000000000
    finney             1000000000000000
    milliether         1000000000000000
    milli              1000000000000000
    ether              1000000000000000000
    kether             1000000000000000000000
    grand              1000000000000000000000
    mether             1000000000000000000000000
    gether             1000000000000000000000000000
    tether             1000000000000000000000000000000
    '''
    if True:
        print (www3.toWei(1, 'ether'))
        print (www3.fromWei(1234567890000000000, 'ether'))


    '''
    # Looking up transactions
    '''
    if True:
        '''
        You can look up transactions using the web3.eth.getTransaction
        function.
        '''
        tx_address = '0x01418168d19aa594d3100dc6cb2e6c4170ba07d0d965001436ce99d0b5a21f6e'
        txn = www3.eth.getTransaction(tx_address)
        print (txn)

        ''' 
        If no transaction for the given hash can be found, then this function
        will instead return None
        '''
        tx_address = '0x00000000d19aa594d3100dc6cb2e6c4170ba07d0d965001436ce990000000000'
        txn = www3.eth.getTransaction(tx_address)
        print (txn)



    '''
    # Looking up receipts
    '''
    if True:
        '''
        Transaction receipts can be retrieved using the
        web3.eth.getTransactionReceipt API.
        '''
        tx_address = '0x01418168d19aa594d3100dc6cb2e6c4170ba07d0d965001436ce99d0b5a21f6e'
        tx_receipt = www3.eth.getTransactionReceipt(tx_address)
        print (tx_receipt)
