# Escreva um script que crie um vetor com 10 posições e receba seus valores do usuário.
# Ao final deverá mostrar somente os valores acima da média.

vetor = [0] * 10
media = 0
soma = 0

for i in range(len(vetor)):
    vetor[i] = float(input(f"Entra com o número {i+1}: "))

for i in range(len(vetor)):
    soma = soma + vetor[i]

media = soma / len(vetor)

# jeito difícil
contador_acima_media = 0
for i in range(len(vetor)):
    if vetor[i] > media:
        contador_acima_media = contador_acima_media + 1

valores_acima_media = [0] * contador_acima_media

j = 0
for i in range(len(vetor)):
    if vetor[i] > media:
        valores_acima_media[j] = vetor[i]
        j += 1

print(media, valores_acima_media)

# jeito mais tranquilo
for i in range(len(vetor)):
    if vetor[i] > media:
        print(vetor[i])


print([a for a in vetor if a > media])

print(list(filter(lambda x : x > media, vetor)))