# Escreva um script que leia 10 números. Ao final deve imprimir em tela:
# 1. o menor valor registrado
# 2. o maior valor registrado
# 3. a média dos valores

maior = -999999999 # sys.maxsize
menor = 9999999999
soma = 0

for i in range(10):
    n = float(input("Entra com o numero " + str(i+1) + ": "))
    if i == 0:
        maior = n
        menor = n
    
    if maior < n:
        maior = n
    if menor > n:
        menor = n

    if n < 0:
        n = -n
        
    soma = soma + n

print(f"Maior: {maior} Menor: {menor} Media: {soma/10}")