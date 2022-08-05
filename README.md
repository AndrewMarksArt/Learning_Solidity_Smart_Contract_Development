# Learning_Solidity_Smart_Contract_Development
Repo for beginner projects while learning Solidity and Smart Contract development

## Will be working through Blockchain Bootcamp 2.0 and adding sample projects / assignments here along with work from BowTiedDevils substack.

### Sample of Topics covered:
1. Development Environment and Package Setup.
   - Linux, Python, Brownie, and other tools
   - Fetching smart contracts from a bloclk explorer, loading into Brownie, interacting with the contract on the console
   - Linux VPS cloud setup for better uptime and latency
   
2. Interacting with the Blockchain Using the Console
   - Router Contracts, send queries to determine swap rates
   - Building a bot to watch swap rates between stablecoin pairs and find arbitrage oportunities
   - Router Contracts, swaps and approvals, set ERC-20 token allowances for future swapping
   - First Console Swap, trade small balance of one stablecoin for another on the console via router contract
   - First Automated Swap, A more complex bot that automates token approval, continuously monitored swap rates between two stablecoins, attempt to exicute arbitrage trade
   - Using a 3rd Party RPC, signing up for 3rd party RPC for better performance
   - Working with ABIs and Unverifed Contracts, loading a contract with an ABI when the source is not published on a block explorer
   - Local Fork with Ganache, Launch a local fork to test bot against a local blockchain copy without spending real money or broadcasting public transactions
   
3. Arbitrage and Bot building
   - High level discussion on AMM's and the role of the Arbitrageur
   - Lessons and examples from successful arbitrage
   - Bot building, structure and helper functions, various helper functions to simplify repetitive botting tasks
   - Bot building, staking rate watcher, simple implementation to track on-chaindata to find arbitrage opportunities
   - Bot building, setup, main loop, and swapping logic
   
4. Uniswap V2
   - Pool reserves I, Calculating swaps directly via formula instead of 'getAmountsOut'
   - Pool Reserves II, partial swaps, improve the calculation to support partial swaps at a target ratio
   - Pool Reserves III, swap and quote function upgrades
   - Querying a UniswapV2 factory contract for liquidity pool addresses
   
5. General EVM and Blockchain
   - Fighting and winning gas wars
   - CHainlink Price Feeds, Calculating Trade EV, Automatically Scaling Gas Fees
   - EV-Based Gas Scaling
   - Event Listeners, accessing built-in "logs" feature to read events emitted when certain blockchain actions occur
   - Asynchronous Websocket Listeners, how to monitor multiple websockets for passive monitoring of events, pending transactions, and new blocks
   - Multicall REquests, batch multiple read-only requests using Brownie, Use multicall feature to retrieve all known liquidity pools on three Avalance DEXs
   
6. Smart COntract Arbitrage
   - Introduction and Overview, high level overview of how atomic smart contract swaps work
   - Toolkit and simple contract, intro to Vyper and using Brownie to deploy and test smart contracts
   - Interfaces, using interfaces to access other smart contracts from our smart contract
   - Flash Borrow Callback, intro to callbaclk feature of UniswapV2 pair contract that enables flash borrowing
   - Two-Pool Flash Swap, simple Vyper contract that performs two-pool atomic flash swap arbitrage
   - Intro to SciPy to quickly calculat optimal inputs for non-linear flach borrow / LP swap arbitrage
   - Better security checks, eliminate use of router in favor of swapping directly at LP contract and reduce gas use
   - Example bot for two-pool arbitrage
   - Calldata Pass-through, ABI Encode/Decode, Flecible Fallback, Pass arbitrary payloads through UniswapV2 callback to eliminate the need for storage vars
   - Generalized Vyper Smart Contracts, intro to generalized EVM bytecode payloads to be exicuted without using an interface
   - Vyper Bundle Executor, general purpose Vyper contract for arbitrage execution of EVM calldata
 
7. Mempool Arbitrage
   - Watch pending transactions before they are confrimed and recorded to the blcokcahin
   - Snowsight, intro to mempool subscription service for Avalanche
   - Using Snowsight transaction propagator, broadcast trades directly to validators (miner) on Snowsight network
   - Snowsight Arbitrage bot, Bot that uses Snowsight to monitor pending transactions and submit trades to the transaction propagator
   - Mempool backrunning, perform mempool transactions backrunning for a simple two-pool arbitrage
   - Predicting the effect of Mempool transactions, generalize the future reserve calculation to support overriding the reserves for any LP in a general arbitrage path
   
8. Graph Theory
   - Find Arbitrage Paths Using Graph Theory and NetworkX, Automatically build arbitrage pathways from available LP info
   - Automatic Arbitrage Path Building, generalize and automate the arbitrage helper generation from the NetworkX pathways
   
9. Infrastructure
   - Running a Local Ethereum Node, use Docker to run a standalone local node instead of using an external RPC
   
   
### Capstone Projects which may be spun out into seperate Repos
- update soon


### External Resources
1. MEV reading
   - update soon
2. Code
   - update soon
3. Videos
   - update soon
4. Smart Contracts
   - update soon
5. Discords
   - update soon
6. Twitter
   - update soon
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
