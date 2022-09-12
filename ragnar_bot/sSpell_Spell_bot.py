from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import sys
import datetime
import time
import requests
import os
import utils
import helpers
from  brownie import *

TRADERJOE_ROUTER_CONTRACT_ADDRESS = utils.TRADERJOE_ROUTER_CONTRACT_ADDRESS
SPELL_CONTRACT_ADDRESS = utils.AVAX_SPELL_CONTRACT_ADDRESS
SSPELL_CONTRACT_ADDRESS = utils.AVAX_SSPELL_CONTRACT_ADDRESS
SNOWTRACE_API_KEY = utils.SNOWTRACE_API_KEY

os.environ["SNOWTRACE_TOKEN"] = SNOWTRACE_API_KEY

def main():
    print("hello, this is the sSpell-Spell bot")


if __name__ == "__main__":
    main()
