# Escreva um script que receba dez nomes do usuário, armazene-os em uma lista e ao final mostre a
# listagem, indicando a ordem de entrada de cada nome.

tamanho = 10
nomes = [""] * tamanho
numeros = [0] * tamanho

for i in range(len(nomes)):
    nomes[i] = input(f"Entra com o nome {i+1}: ")

for i in range(len(nomes)):
    print(f"{i+1}: {nomes[i]}")
