"""
TODO:
[SETUP]
Connect to the network
Load the user account
Load the router contract
Load the token contracts

[DATA STRUCTURES]
Prepare a data structure for each token
Prepare a data structure for each unique token pair

[MAIN PROGRAM]
Set up loop
Fetch and store swap rates
Print interesting results 
"""

# for [SETUP]
import time
import datetime
from brownie import *

user = accounts.load('test_account')
network.connect('avax-main')

print("Loading COntracts:")
dai_contract = Contract.from_explorer('0xd586e7f844cea2f87f50152665bcbc2c279d8d70')
mim_contract = Contract.from_explorer('0x130966628846bfd36ff31a822705796e8cb8c18d')
usdc_contract = Contract.from_explorer('0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664')
usdt_contract = Contract.from_explorer('0xc7198437980c041c805a1edcba50c1ce5db95118')
wavax_contract = Contract.from_explorer('0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7')
router_contract = Contract.from_explorer('0x60aE616a2155Ee3d9A68541Ba4544862310933d4')
