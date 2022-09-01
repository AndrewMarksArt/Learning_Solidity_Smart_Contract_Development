# import needed packages
import time
import datetime
from brownie import *


def main():
    # load user test_account
    # if need to create account run
    user = accounts.load('test_account2')

    # connect to avax network
    network.connect('avax-main')

    # load router and stable coin contracts
    print("Loading Contracts:")
    dai_contract = Contract.from_explorer('0xd586e7f844cea2f87f50152665bcbc2c279d8d70')
    mim_contract = Contract.from_explorer('0x130966628846bfd36ff31a822705796e8cb8c18d')
    usdc_contract = Contract.from_explorer('0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664')
    usdt_contract = Contract.from_explorer('0xc7198437980c041c805a1edcba50c1ce5db95118')
    wavax_contract = Contract.from_explorer('0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7')
    router_contract = Contract.from_explorer('0x60aE616a2155Ee3d9A68541Ba4544862310933d4')

    # create dictionaries to store the data for each stablecoin
    dai = {
        "address": dai_contract.address,
        "symbol": dai_contract.symbol(),
        "decimals": dai_contract.decimals(),
    }

    mim = {
        "address": mim_contract.address,
        "symbol": mim_contract.symbol(),
        "decimals": mim_contract.decimals(),
    }

    usdc = {
        "address": usdc_contract.address,
        "symbol": usdc_contract.symbol(),
        "decimals": usdc_contract.decimals(),
    }

    usdt = {
        "address": usdt_contract.address,
        "symbol": usdt_contract.symbol(),
        "decimals": usdt_contract.decimals(),
    }

    # create a list of token pairs tuples
    # each pair is listed twice as (a, b) and (b, a)
    # these will be compaired later to try and find arb opportunities
    token_pairs = [
        (dai, mim),
        (mim, dai),
        (dai, usdc),
        (usdc, dai),
        (usdt, dai),
        (dai, usdt),
        (usdc, usdt),
        (usdt, usdc),
        (usdt, mim),
        (mim, usdt),
        (usdc, mim),
        (mim, usdc),
    ]

    # we want to run continuously so we use a while True loop
    print("looking for arbs...")
    while True:
        # for each token pair in the token pair list
        for pair in token_pairs:
            # set token in as the coin being sent in
            token_in = pair[0]
            # set token out as the coin we want to get out
            token_out = pair[1]
            # use getAmountsOut to see how much 1 of token in will swap for token out
            # save just the amount of token out we will get for 1 token in
            qty_out = (
                router_contract.getAmountsOut(
                    1 * (10 ** token_in["decimals"]), 
                    [
                        token_in["address"],
                        wavax_contract.address,
                        token_out["address"],
                    ],
                )[-1] / (10 ** token_out["decimals"])
            )
            # check to see if the there is a 1% or greater difference between the pairs
            # these are actionable trades that have a minimum profit of at least 1%
            # only print out profitable trades
            if qty_out >= 1.01:
                print(
                    f"{datetime.datetime.now().strftime('[%I:%M:%S %p]')} {token_in['symbol']} → {token_out['symbol']}: ({qty_out:.3f})"
                )
            # wait for 0.1 seconds
            time.sleep(0.1)

if __name__ == "__main__":
    main()