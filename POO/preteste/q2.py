matriz = [[0 for _ in range(3)] for __ in range(5)]

for i in range(5):
    for j in range(3):
        matriz[i][j] = float(input(f"Digite o valor [{i+1},{j+1}]: ")) 

soma = 0 
for i in range(5):
    for j in range(3):
        soma += matriz[i][j]

media = sum(soma) / len(5*3)

print("Menores:")
for i in range(5):
    for j in range(3):
        if matriz[i][j] < media:
            print(matriz[i][j])

print("Maior:")
for i in range(5):
    for j in range(3):
        if matriz[i][j] > media:
            print(matriz[i][j])
