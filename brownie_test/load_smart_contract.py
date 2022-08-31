import subprocess

def main():
    # start brownie console
    subprocess.run("brownie console --network avax-main")

    # TODO: figure out how to do all this in program but for now
    # list commands to run once brownie console is active

    # load the test account
    user = "accounts.load('test_account')"
    # enter user password

    # load wavax contract
    wavax_contract = "Contract.from_explorer('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')"

    # take a look at the contract
    dir(wavax_contract)
    # check the address and balance
    wavax_contract.address
    wavax_contract.balance()

    # very similar to using PublicKeyAccount() but some interesting new items
    wavax_contract.decimals()
    wavax_contract.balanceOf('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')

    """
    blockchain ledger must maintain perfect accuracy but with floating point numbers that
    can be tricky. So instead of floating point numbers Ethereum and othe EVM chains utilize
    high bit integers with a seperate value for the decimal plasce associated with that value.
    This way the chains offer up to 256 bit integer precision on all numbers.

    so to figure out the real balance you need to take the balance() / (10 ** .decimals())
    """

    wavax_contract.balance() / (10 **wavax_contract.decimals())



if __name__ == "__main__":
    main()
