from datetime import date, datetime
from time import sleep
from typing import Union

from colorama import Fore


def date_para_str(data: date) -> str:

    try:
        return data.strftime('%d/%m/%Y')
    except ValueError:
        print(Fore.RED + 'Data de nascimento inválida.')
        sleep(2.5)


def str_para_date(data: str) -> Union[datetime, bool]:

    try:
        return datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        return False


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'

