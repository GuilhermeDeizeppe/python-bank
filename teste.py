from models.cliente import Cliente
from models.contas import Conta


felicity: Cliente = Cliente('Felicity Jones', 'felicity@jones.com', '123.456.789-01', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@jolie.com', '987.654.321-09', '08/07/1978')

conta_f: Conta = Conta(felicity)
conta_a: Conta = Conta(angelina)

# print(conta_f)
# print(conta_a)


