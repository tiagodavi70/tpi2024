class ContaBancaria:
    def __init__(self, saldo_inicial=20):
        self.__saldo = saldo_inicial

    def depositar(self, valor): 
        self.__saldo = self.__saldo + valor
    def levantar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")
    
    def mostrar_saldo(self):
        return self.__saldo

 # Utilização
conta = ContaBancaria(100)
conta.depositar(50)
print(conta.mostrar_saldo())
conta.levantar(200)
print(conta.mostrar_saldo())

contaSemValor = ContaBancaria()
print(contaSemValor.mostrar_saldo())

import random
contas = [None] * 10
for i in range(10):
    contas[i] = ContaBancaria(random.randint(20,700))

for i in range(10):
    print(contas[i].mostrar_saldo())