from random import randint
from time import sleep

from config import sleep_accs, sleep_accs_from, sleep_accs_to


def newersleep_accs() -> None:
    if sleep_accs:
        sleep(randint(sleep_accs_from, sleep_accs_to))
