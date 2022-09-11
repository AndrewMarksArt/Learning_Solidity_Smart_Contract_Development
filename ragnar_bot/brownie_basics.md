### learning how to use brownie on the comand line

from terminal use "brownie accounts generate " {account name} to create an account/wallet address
it will ask for a password and then generate a 12 word mnemomic phrase and you can create an
account with a known private key.

// create new wallet/account
"brownie accounts create <id>" 

### Using the console
"brownie networks modify avax-main" to show network id, chainid, explorer, and host

"brownie console --network avax-main" opens a python console

user = accounts.load({account name}) --> loads the account created from above

dir(user) to see to explore the user object --> user.address, user.balance(), etc.

### lets look at another wallet with funds in it
someone_eles = network.account.PublicKeyAccount('0xB31f66AA3C1e7853
63F0875A1B74E27b85FD66c7')

someone_else.balance()

this is the Wrapped AVAX contract so has a large balance, see more on [SnowTrace](https://snowtrace.io/address/0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7)