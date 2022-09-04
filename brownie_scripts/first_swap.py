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

    # get wavx contract needed for swaps
    wavax = Contract.from_explorer('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')

    # swap AVAX for exact tokens
    router.swapAVAXForExactTokens(
        5*(10**mim.decimals()),
        [wavax.address, mim.address],
        # address the new tokens swaped for will go
        user.address,
        # deadline, UNIX time in sec but blockchain wants milliseconds
        # get time convert to milliseconds and add 30 seconds for txs
        1000*int(time.time()+30),
        # from what address, and max value of avax to be used
        {'from': user.address, 'value': 0.2*10**18}
    )

    # print MIM balance after the swap
    print(f"{mim.balanceOf(user.address)}")
    # more readable balance print out
    print(f"{mim.balanceOf(user.address/(10**mim.decimals()))}")

    # set approval for MIM
    mim.approve(router.address, 2.5*10**mim.decimals(), {'from': user.address})
    # print MIM allowance for MIM
    print(f"{mim.allowance(user.address)}")
    # more readable balance print out
    print(f"{mim.allowance(user.address/(10**mim.decimals()))}")

    # swap MIM for DAI
    router.swapExactTokensForTokens(
        # how much MIM to swap
        2.5*10**mim.decimals(),
        # minimum DAI --> exchange rate set to 0.95
        0.95*2.5*10**dai.decimals(),
        [mim.address, dai.address],
        # address output will go to
        user.address,
        # deadline --> 30 second limit and convert to milliseconds
        1000*int(time.time()+30),
        # from address
        {'from': user.address}
    )

    # Print Balances of MIM, DAI, and AVAX
    print("Balances after swaps:")
    # print MIM balance after the swap
    print(f"MIM balance: {mim.balanceOf(user.address)}")
    print(f"MIM balance: {mim.balanceOf(user.address/(10**mim.decimals()))}")

    # print DAI balance after the swap
    print(f"DAI balance: {dai.balanceOf(user.address)}")
    print(f"DAI balance: {dai.balanceOf(user.address/(10**dai.decimals()))}")

    # print AVAX balance after the swap
    print(f"AVAX balance: {user.balance()}")
    print(f"AVAX balance: {user.balance()/(10**wavax.decimals())}")


if __name__ == "__main__":
    main()
