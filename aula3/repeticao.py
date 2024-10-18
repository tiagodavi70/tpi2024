cont = 0
for i in range(5):
    # entrada = int(input("Entra com um numero: "))
    entrada  = input()
    entrada = int(entrada)
    if entrada < 0:
        cont += 1
print("Total de negativos:", cont)

