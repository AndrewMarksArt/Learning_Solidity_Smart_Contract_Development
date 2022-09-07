import sys
import time
import datetime
import requests
import os
import brownie

import utils

# get api key
os.environ["SNOWTRACE_TOKEN"] = utils.SNOWTRACE_API_KEY

# bot options that can be toggled
# simulate swaps and approvals
DRY_RUN = False
# quit after first successful trade
ONE_SHOT = False
# how often to run the main loop (in seconds)
LOOP_TIME = 1.0

# Swap thresholds
# SPELL --> sSPELL swap targets
# 1. a zero value will trigger a swap when the ratio matches base_staking_rate exactly
# 2. a negative value will trigger a swap when the rate is below the base_staking_rate
# 3. a pasitive value will trigger a swap when the rate is above the base_staking_rate
THRESHOLD_SPELL_TO_SSPELL = 0.2 * utils.PERCENT

# sSPELL --> SPELL swap targets
# a positive value  will triger a (sSPELL -> SPELL) swap when the ratio is above base_staking_rate
THRESHOLD_SSPELL_TO_SPELL = 1.2 * utils.PERCENT

# tolerated slippage in swap price (used to calculate amountOutMin)
SLIPPAGE = 0.1 * utils.PERCENT

def main():
    


if __name__ == "__main__":
    main()
