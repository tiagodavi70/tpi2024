# Escreva um script que faça uma multiplicação entre dois números, através de sucessivas somas.
# 5*3=15
# 5+5+5=15
# 3+3+3+3+3=15

num1 = int(input("Entra com o numero 1: "))
num2 = int(input("Entra com o numero 2: "))

soma = 0
for i in range(num2):
    soma = soma + num1
print("Soma: ", soma)