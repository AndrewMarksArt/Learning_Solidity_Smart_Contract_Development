# exploring the Uniswap V2 Router contract and looking at token-for-token swaps
# most DEXes are clones of Uniswap, even sushi swap started as a simple fork
# learning how to use Uniswap V2 will alow you to move your knowledge to most
# other DEXes very quickly

from brownie import *

def main():

    # load the test account and connect to network
    user = accounts.load('test_account')
    network.connect('avax-main')

    # load contracts to use when exploring "getAmountsOut()"
    router_contract = Contract.from_explorer('0x60aE616a2155Ee3d9A68541Ba4544862310933d4')
    usdc_contract = Contract.from_explorer('0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e')
    usdt_contract = Contract.from_explorer('0xc7198437980c041c805a1edcba50c1ce5db95118')
    wavax_contract = Contract.from_explorer('0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7')

    # getAmountsOut() needs an unsigned integer specifying the number of tokens sent to the router
    # then a Solidity array containing addresses of all tokens involved in the proposed swap
    # starting with the one that you want to swap in and ending with the token that you want to recieve out.
    # brownie will automatically translate the built-in list data structure inow a proper Solidity Array.

    # NOTE about the address array -- a token swap can only be done by passing the input token through
    # a liquidity pool or series of pools. Some have dedicated pools but most go through and intermediate
    # wrapper pool reducing the number of pools needed to swap.

    # NOTE this is handled for you automatically on the web front end but intermediate token address
    # must be added to your Brownie calls

    router_contract.getAmountsOut(
                                    1*(10**usdt_contract.decimals()), 
                                    [usdt_contract.address, wavax_contract.address, usdc_contract.address]
                                )

    # will be (usdt amount of tokens, wavax amount of tokens, and usdc amount of tokens)
    # middle number will be much larger than the others because usdt and usdc use 6 decimals not 18 like wavax
    usdt_dec = usdt_contract.decimals()   # should be 6
    usdc_dec = usdc_contract.decimals()   # should be 6
    wavax_dec = wavax_contract.decimals()  # should be 18

    print(usdt_dec, usdc_dec, wavax_dec)
    # we dont care about the number of wavax if swapping from usdt to usdc so add [-1] at the end of getAmountsOut()
    # to display the last items which is usdc then divide by 10 ^ usdc.decimals() to get a more readable output
    usdt_usdc = router_contract.getAmountsOut(
                                              1*(10**usdt_contract.decimals()), 
                                              [usdt_contract.address, wavax_contract.address, usdc_contract.address]
                                             )[-1]/(10**usdc_contract.decimals())

    # print out the usdt --> usdc swap rate
    print(usdt_usdc)

    
    # run the reverse to see usdc --> usdt
    usdc_usdt = router_contract.getAmountsOut(
                                              1*(10**usdc_contract.decimals()), 
                                              [usdc_contract.address, wavax_contract.address, usdt_contract.address]
                                             )[-1]/(10**usdt_contract.decimals())
    # print out the usdc --> usdt swap rate
    print(usdc_usdt)


if __name__ == "__main__":
    main()
