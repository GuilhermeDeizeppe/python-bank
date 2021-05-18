from models.cliente import Cliente
from utils.helper import formata_float_str_moeda
from colorama import Fore


class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Número da Conta: {self.numero}.\nCliente: {self.cliente.nome}.' \
               f'\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:

        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print(Fore.LIGHTGREEN_EX + 'Depósito efetuado com sucesso.')
        else:
            print(Fore.RED + 'Algo deu errado. Verifique o valor e tente novamente.')

    def sacar(self: object, valor: float) -> None:

        if valor > 0 and self.saldo_total >= valor:

            if self.saldo >= valor:

                self.saldo -= valor
                self.saldo_total = self._calcula_saldo_total

            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total

            print(Fore.LIGHTGREEN_EX + 'Saque efetuado com sucesso!')

        else:
            print(Fore.RED + 'Saque não autorizado. Tente novamente.')

    def transferir(self: object, destino: object, valor: float):

        if self != destino:

            if valor > 0 and self.saldo_total >= valor:

                if self.saldo >= valor:

                    self.saldo -= valor
                    self.saldo_total = self._calcula_saldo_total
                    destino.saldo += valor
                    destino.saldo_total = destino._calcula_saldo_total
                else:
                    restante: float = self.saldo - valor
                    self.saldo = 0
                    self.limite += restante
                    self.saldo_total = self._calcula_saldo_total
                    destino.saldo += valor
                    destino.saldo_total = destino._calcula_saldo_total

                print(Fore.LIGHTGREEN_EX + 'Transferência efetuada com sucesso!')

            else:
                print(Fore.RED + 'Transferência não autorizada. Tente novamente.')
        else:
            print(Fore.RED + 'As contas de origem e destino devem ser diferentes.')
