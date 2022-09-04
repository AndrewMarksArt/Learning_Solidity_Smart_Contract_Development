# atempt to make a swap from the console using brownie
import time
from brownie import *


def main():
    # set the users account
    # enter password when prompted
    user = accounts.load("Ragnar")

    # connect to network
    network.connect('avax-main')

    # check user balance and print it out
    # make sure to divide by 10^decimals(18)
    print(f"Users AVAX balance: {user.balance()/(10**18)}")

    # set the router --> Trader Joe router address
    router = Contract.from_explorer('0x60aE616a2155Ee3d9A68541Ba4544862310933d4')

    # get contracts for stables --> MIM DAI
    mim = Contract.from_explorer('0x130966628846bfd36ff31a822705796e8cb8c18d')
    dai = Contract.from_explorer('0xd586e7f844cea2f87f50152665bcbc2c279d8d70')

    # check user balances and allowences for the stables
    print("Balances:")
    print(f"User MIM balance: {mim.balanceOf(user.address)}")
    print(f"User DAI balance: {dai.balanceOf(user.address)}")
    print("Allowances:")
    print(f"User MIM allowance: {mim.allowance(user.address, router.address)}")
    print(f"User DAI allowance: {dai.allowance(user.address, router.address)}")


if __name__ == "__main__":
    main()
