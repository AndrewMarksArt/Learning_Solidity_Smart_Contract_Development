# atempt to make a swap from the console using brownie
from brownie import *


def main():
    # set the users account
    # enter password when prompted
    user = accounts.load("Ragnar")

    # connect to network
    network.connect('avax-main')

    # print the users balance
    # make sure to divide by 10^decimals(18)
    print(user.balance()/(10**18))


if __name__ == "__main__":
    main()
