# Escreva um algoritmo que leia um valor como saldo, e depois leia um valor de
# levantamento e apresente quanto saldo ainda resta

saldo = input("Entra com o saldo: ")
retirada = input("Entra com o valor de retirada: ")

saldo = float(saldo)
retirada = float(retirada)

print("Valor disponível: ", saldo - retirada)