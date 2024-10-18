# Escreva um script que conte:
# a) de 1 até n
# b) de n até n/2 saltando de 3 em três
# c) de 1 até n2 os divisíveis por 4

n = int(input("Entra com o n: "))
for i in range(1, n+1):
    print(i)

for i in range(n, n//2, -3):
    print(i)

for i in range(1,n):
    if i % 4 == 0:
        print(i)