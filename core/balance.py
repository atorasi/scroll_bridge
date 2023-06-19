from web3 import Web3

from utils import script_exceptions


@script_exceptions
def balance_check(private_key: str, rpc: str) -> float:
    w3 = Web3(Web3.HTTPProvider(rpc))
    
    account = w3.eth.account.from_key(private_key)
    adres = account.address
    balance = w3.eth.get_balance(adres)
    balance_eth = float(w3.from_wei(balance, 'ether'))
    
    return balance_eth
            

            

        