# Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias. Todo mês tem 30 dias e todo ano tem 365.

anos = input("Qual sua idade? ")
meses = input("Quantos meses desde de o seu aniverário? ")
dias = input("Quantos dias? ")

anos = int(anos)
meses = int(meses)
dias = int(dias)

print("Você viveu", (anos * 365) + (meses * 30) + dias, "dias")

