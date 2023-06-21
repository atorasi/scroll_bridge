from random import randint

from utils import logger
from config import rpc, percent_sc_from, percent_sc_to
from core import balance_check, bridge_geth



if __name__ == "__main__":
    with open('private_keys.txt', 'r') as file:
        keys = [row.strip() for row in file]
        
    for acc_num, key in enumerate(keys, start=1):
        acc_info = f'Acc.|-{acc_num}-|-{key[:3]}. . .{key[-3:]}-|'

        eth_balance = balance_check(key, rpc['goerli'])
        logger.info(f'{acc_info} Баланс в gETH - {eth_balance}')

        scroll_balance, temp = balance_check(key, rpc['scroll']), balance_check(key, rpc['scroll']) 
        logger.info(f'{acc_info} Баланс в SCROLL - {scroll_balance}') 
        
        value_to_scroll = eth_balance * randint(percent_sc_from * 1_000, percent_sc_to * 1_000) / 100_000
        scroll_bridge_hash = bridge_geth(key, rpc['goerli'], value_to_scroll)
        logger.success(f'{acc_info} Отправил gETH --> SCROLL, используя Scroll Alpha')
        logger.info(f'Сплю {newersleep_accs()} секунд, перед некст акком.')
        
