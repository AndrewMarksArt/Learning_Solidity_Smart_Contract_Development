from http.client import TOO_MANY_REQUESTS
import time
import datetime
import sys
from brownie import *


def main():
    """
    Program overview:
    3 Stages
        1. set up
            a. connect to the network
            b. load the user account
            c. load the router contract
            d. load the token contracts
        2. data structures
            a. prepare a data structure for each token
        3. main program
            a. get allowance and set approvals
            b. set up loop
            c. fetch, store, and print swap rates
            d. print interesting results
            e. execute a swap if the threshold is met
    """

    # connect to avax network
    network.connect('avax-main')
    print(f'Connected to {network.show_active()} network')
    # load user account
    user = accounts.load("Ragnar")

    # load the contracts
    print("Loading Contracts:")
    dai_contract = Contract.from_explorer('0xd586e7f844cea2f87f50152665bcbc2c279d8d70')
    mim_contract = Contract.from_explorer('0x130966628846bfd36ff31a822705796e8cb8c18d')
    wavax_contract = Contract.from_explorer('0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7')
    router_contract = Contract.from_explorer('0x60aE616a2155Ee3d9A68541Ba4544862310933d4')
    time.sleep(2)

    # create data structure for each token
    dai = {
        "address": dai_contract.address,
        "symbol": dai_contract.symbol(),
        "decimals": dai_contract.decimals(),
        "balance": dai_contract.balanceOf(user.address)
    }

    mim = {
        "address": mim_contract.address,
        "symbol": mim_contract.symbol(),
        "decimals": mim_contract.decimals(),
        "balance": mim_contract.balanceOf(user.address)
    }

    # print out the details for both tokens
    print(dai)
    print(mim)

    # if mim balance is 0 exit
    if mim["balance"] == 0:
        sys.exit("MIM balance is zero, aborting...")

    # confirm approvals and allowences
    # want to swap the remaining mim to dai so make sure allowence is atleast the balance
    if mim_contract.allowance(user.address, router_contract.address) < mim["balance"]:
        mim_contract.approve(
            router_contract.address,
            mim["balance"],
            {'from': user.address}
        )

    last_ratio = 0.0

    while True:
        try:
            qty_out = router_contract.getAmountsOut(
                mim["balance"],
                [
                    mim["address"],
                    wavax_contract.address,
                    dai["address"]
                ],
            )[-1]
        except:
            print("ran into an error, retrying...")
            continue

        ratio = round(qty_out / mim["balance"], 3)
        if ratio != last_ratio:
            print(f"{datetime.datetime.now().strftime('[%I:%M:%S %p]')} MIM --> DAI: ({ratio:.3f})")
            last_ratio = ratio

        if ratio >= 0.997:
            print("*** Executing Swap ***")
            try:
                router_contract.swapExactTokensForTokens(
                    mim["balance"],
                    int(0.995 * qty_out),
                    [
                        mim["address"],
                        wavax_contract.address,
                        dai["address"]
                    ],
                    user.address,
                    1000 * int(time.time() + 60),
                    {'from': user}
                )
                print("Swap Successful!")
            except:
                print("Swap failed, better luck next time!")
            finally:
                break
        
        time.sleep(0.5)


if __name__ == "__main__":
    main()
