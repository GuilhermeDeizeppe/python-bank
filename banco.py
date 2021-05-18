import colorama
from colorama import Fore, Back, Style
from typing import List
from time import sleep
from models.cliente import Cliente
from models.contas import Conta
from utils.helper import str_para_date


colorama.init(autoreset=True)

contas: List[Conta] = []


def main() -> None:

    print(Fore.LIGHTCYAN_EX + '==========================================================')

    print(Fore.LIGHTCYAN_EX + '==================== ' + Fore.LIGHTYELLOW_EX + 'CAIXA ELETRÔNICO' +
          Fore.LIGHTCYAN_EX + ' ====================')

    print(Fore.LIGHTCYAN_EX + '====================== ' + Fore.LIGHTYELLOW_EX + 'BANQUINHO S/A'
          + Fore.LIGHTCYAN_EX + ' =====================')

    print(Fore.LIGHTCYAN_EX + '==========================================================')

    menu()


def menu() -> None:

    print(Fore.BLUE + '\nServiços Disponíveis: ')
    print('1 - Abrir Conta')
    print('2 - Saques')
    print('3 - Depósitos')
    print('4 - Transferências')
    print('5 - Listar Contas')
    print('6 - Extrato')
    print('7 - Encerrar sessão')

    try:
        opcao: int = int(input(Fore.BLUE + '\nDigite o sistema desejado: '))
    except ValueError:
        print('\n' + Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + 'Opção inválida:' + Style.RESET_ALL +
              ' certifique-se de digitar o número do sistema corretamente.')
        sleep(2)
        menu()

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        puxar_extrato()
    elif opcao == 7:
        print(Fore.LIGHTGREEN_EX + 'Sessão encerrada com segurança.')
        sleep(2)
        exit(0)
    else:
        print('\n' + Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + 'Opção inválida:' + Style.RESET_ALL +
              ' verifique o número digitado.')
        sleep(2)
        menu()


def criar_conta() -> None:

    print('\n' + Fore.BLUE + 'Abertura de Contas')

    nome: str = input('Nome do Cliente: ')
    email: str = input('E-mail do Cliente: ')
    cpf: str = input('CPF do Cliente: ')
    data_nascimento: str = input('Data de Nascimento do Cliente: ')

    for conta in contas:
        if cpf == conta.cliente.cpf:
            print(Fore.RED + 'Já existe uma conta vinculada ao CPF informado.')
            sleep(3)
            menu()

    if str_para_date(data_nascimento):
        pass
    else:
        print(Fore.RED + 'Data de nascimento inválida.')
        sleep(2.5)
        menu()

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print(Back.YELLOW + Fore.LIGHTWHITE_EX + 'Abertura de Conta concluída!')
    print()
    sleep(2)
    print(Fore.BLUE + 'Dados da nova Conta: ')
    print(conta)
    sleep(3.5)
    menu()


def efetuar_saque() -> None:

    if len(contas) > 0:
        print('\n' + Fore.BLUE + 'Efetuar Saque')

        try:
            numero: int = int(input('Informe o número da conta: '))
            conta: Conta = buscar_conta_por_numero(numero)
        except ValueError:
            print(Fore.RED + 'Número da conta inválido.')
            sleep(2.5)
            menu()

        if conta:

            try:
                valor: float = float(input('Valor do saque: '))
                conta.sacar(valor)
                sleep(2)
            except ValueError:
                print(Fore.RED + 'Valor inválido.')
                sleep(2)
                menu()
        else:
            print(Fore.RED + f'Conta {numero} não encontrada.')
            sleep(2)

    else:
        print('Ainda não existem contas abertas.')
        sleep(2)
        menu()

    menu()


def efetuar_deposito() -> None:

    if len(contas) > 0:
        print('\n' + Fore.BLUE + 'Efetuar Depósito')

        try:
            numero: int = int(input('Informe o número da conta: '))
            conta: Conta = buscar_conta_por_numero(numero)
        except ValueError:
            print(Fore.RED + 'Número da conta inválido.')
            sleep(2.5)
            menu()

        if conta:

            try:
                valor: float = float(input('Valor do depósito: '))
                conta.depositar(valor)
                sleep(2)
            except ValueError:
                print(Fore.RED + 'Valor inválido.')
                sleep(2)
                menu()
        else:
            print(Fore.RED + f'Conta {numero} não encontrada.')
            sleep(2)

    else:
        print('Ainda não existem contas abertas.')
        sleep(2)
        menu()

    menu()


def efetuar_transferencia() -> None:

    if len(contas) > 0:
        print('\n' + Fore.BLUE + 'Efetuar Transferência')

        try:
            numero_o: int = int(input('Informe o número da conta de origem: '))
            conta_o: Conta = buscar_conta_por_numero(numero_o)
        except ValueError:
            print(Fore.RED + 'Número da conta de origem inválido.')
            sleep(2.5)
            menu()

        if conta_o:

            try:
                numero_d: int = int(input('Informe o número da conta de destino: '))
                conta_d: Conta = buscar_conta_por_numero(numero_d)
            except ValueError:
                print(Fore.RED + 'Número da conta de destino inválido.')
                sleep(2.5)
                menu()

            if conta_d:

                try:
                    valor: float = float(input('Valor da Transferência: '))
                    conta_o.transferir(conta_d, valor)
                    sleep(2)
                except ValueError:
                    print(Fore.RED + 'Valor inválido')
                    sleep(2)
                    menu()

            else:
                print(Fore.RED + f'Conta de destino {numero_d} não encontrada.')
                sleep(2)
        else:
            print(Fore.RED + f'Conta de origem {numero_o} não encontrada.')
            sleep(2)
    else:
        print('Ainda não existem contas abertas.')
        sleep(2)
        menu()

    menu()


def listar_contas() -> None:

    if len(contas) > 0:
        print('\n' + Fore.BLUE + 'Listagem de Contas\n')

        for conta in contas:
            print(conta)
            print(Fore.BLUE + '------------------------')
            sleep(0.7)
    else:
        print('Ainda não existem contas abertas.')
        sleep(2)
        menu()

    menu()


def buscar_conta_por_numero(numero: int) -> None:
    c: Conta = None

    if len(contas) > 0:

        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


def puxar_extrato() -> None:

    if len(contas) > 0:

        print('\n' + Fore.BLUE + 'Emissão de Extrato')

        try:
            numero: int = int(input('Digite o número da conta: '))
            conta: Conta = buscar_conta_por_numero(numero)

            if conta == None:
                print(Fore.RED + f'Conta {numero} não localizada.')
                sleep(2.5)
                menu()

        except ValueError:
            print(Fore.RED + 'Número da conta inválido.')
            sleep(2.5)
            menu()

        print()
        print(conta)
        print('------------------------')
        sleep(0.5)

    else:
        print('Ainda não existem contas abertas.')
        sleep(2)
        menu()

    menu()


if __name__ == '__main__':
    main()
