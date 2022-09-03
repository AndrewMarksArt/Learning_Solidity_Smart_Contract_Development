# imports
from brownie import *

"""
focus of this file is to examine swapExactTokensForTokens()
part of Uniswap V2 Router Contract and is structured like:

function swapExactTokensForTokens(uint amountIn, uint amountOutMin,
address[], calldata path, address to, uint deadline) external
returns(uint[] memory amounts)

IMPORTANT NOTE from Uniswap Docs:
msg.sender should have already given the router an allowance of at
least amountIn on the imput token.

token approval is granted by calling approve() on a token contract,
authorizing another address to withdraw tokens up to the amount specified.

NOTE if you grant approval for an address to withdraw a token on your behalf,
it maydo so at any time for any reason without needing any interaction from you

NOTE good practice should be to only set approval to the amount you want to
swap at any given time and then immediately set it back to 0 once completed.
"""


def main():
    # in order to swap first we need to grant approval
    # load users account
    user = accounts.load('test_account2')
    # load router contract
    router_contract = Contract.from_explorer(
        '0x60aE616a2155Ee3d9A68541Ba4544862310933d4'
        )
    # load MIM coin contract
    mim = Contract.from_explorer(
        '0x130966628846bfd36ff31a822705796e8cb8c18d'
    )
    # approve MIM --> [APPROVAL AMOUNT] is a placeholder
    # Approval Amount is represented by a 256-bit unsigined integer
    # which can take any value from 0 up to (2 ** 256-1)
    # use (2 ** 256-1) for "unlimited approval", use 0 to "revoke"

    # NOTE the unsigned integer value is the ETH token quantity,
    # so it should always be multipled by (10 ** decimal())
    # for USDT (6 decimal places) --> (10 ** 6)
    mim.approve(
        router_contract.address,
        [APPROVAL AMOUNT],
        {'from': user}
    )

    # SLippage = allowed price difference between the submitted swap
    # and the executed swap, common to see 0.5%-1% for normal pairs
    # and up to 5% for low volume pairs --> but this is BAD
    # NOTE ther is no slippage parameter, is made up to improve the
    # UX when swapping on a DEX


if __name__ == "__main__":
    main()
