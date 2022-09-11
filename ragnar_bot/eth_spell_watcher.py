import sys
import time
import os
from brownie import *

# Change these to match the Project ID from https://infura.io
WEB3_INFURA_PROJECT_ID = "018a028e27844d9cb77f2f6b08beff91"

SPELL_CONTRACT_ADDRESS = "0x090185f2135308bad17527004364ebcc2d37e5f6"
SSPELL_CONTRACT_ADDRESS = "0x26FA3fFFB6EfE8c1E69103aCb4044C26B9A106a9"

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
    spell_contract = contract_load(SPELL_CONTRACT_ADDRESS, "Token: SPELL")
    sspell_contract = contract_load(SSPELL_CONTRACT_ADDRESS, "Token: sSPELL")

    print("\nCreating new file:")
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


def contract_load(address, alias):
    # Attempts to load the saved contract.
    # If not found, fetch from network explorer and save.
    try:
       contract = Contract(alias)
    except ValueError:
        contract = Contract.from_explorer(address)
        contract.set_alias(alias)
    finally:
        print(f"• {alias}")
        return contract


# Only executes main loop if this file is called directly
if __name__ == "__main__":
    main()
