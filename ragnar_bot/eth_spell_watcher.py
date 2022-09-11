import sys
import time
import os
from brownie import *
import utils
import helpers

# Change these to match the Project ID from https://infura.io
WEB3_INFURA_PROJECT_ID = utils.WEB3_INFURA_PROJECT_ID

SPELL_CONTRACT_ADDRESS = utils.ETH_SPELL_CONTRACT_ADDRESS
SSPELL_CONTRACT_ADDRESS = utils.ETH_SSPELL_CONTRACT_ADDRESS

os.environ["WEB3_INFURA_PROJECT_ID"] = WEB3_INFURA_PROJECT_ID

FILENAME = ".abra_rate"


def main():
    
    try:
        network.connect("mainnet")
    except:
        sys.exit(
            "Could not connect to Ethereum! Verify that brownie lists the Ethereum (Infura) Mainnet using 'brownie networks list'"
        )

    print("\nContracts loaded:")
    spell_contract = helpers.contract_load(SPELL_CONTRACT_ADDRESS, "Token: SPELL")
    sspell_contract = helpers.contract_load(SSPELL_CONTRACT_ADDRESS, "Token: sSPELL")

    print("\nCreating/opening file:")
    # creates a blank file, writes "0.0" to force a refresh in the main loop
    with open(FILENAME, "w") as file:
        file.write(str(0.0) + "\n")

    print("\n Begin while true loop: ")
    while True:
        with open(FILENAME, "r") as file:
            abra_rate = float(file.read().strip())

        try:
            result = round(
                spell_contract.balanceOf(sspell_contract.address)
                / sspell_contract.totalSupply(),
                4,
            )
        except Exception as e:
            print(f"{e}")
            continue

        if abra_rate and result == abra_rate:
            pass
        else:
            print(f"Updated rate found: {result}")
            abra_rate = result
            with open(FILENAME, "w") as file:
                file.write(str(abra_rate) + "\n")

        time.sleep(60)


# Only executes main loop if this file is called directly
if __name__ == "__main__":
    main()
