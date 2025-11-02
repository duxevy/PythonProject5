from typing import Generator

def card_number_gen(start: int, stop: int) -> Generator:
    """"""
    for n in range(start, stop+1):
        n_str = str(n)
        while len(n_str) < 16:
            n_str = "0" + n_str
        card_number = f"{n_str[:4]} {n_str[4:8]} {n_str[8:12]} {n_str[12:]}"
        yield card_number

for i in card_number_gen(9999, 10003):
    print(i)