# import random
# vetor = [random.random() for _ in range(6)]

vetor = [0] * 6
for i in range(6):
    vetor[i] = int(input("Digite um valor para dar entrada ao vetor: "))

n = int(input("Digite um valor para somar ao vetor: "))
for i in range(6):
    vetor[i] = vetor[i] + n

print("Vetor com soma:", vetor)