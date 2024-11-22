# Escreva um script que dado dois vetores indique os elementos
# que estão presentes nos dois vetores.
import random 

def elementosIguais(a, b):

    for itemA in a:
        for itemB in b:
            # print(a[i], b[j])
            if itemA == itemB:
                print("igual", itemA)

a = [1, 2, 3, 4, 40, 50, 60, 8]
b = [4, 5, 6, 2]
# c = [4,2]
elementosIguais(a, b)

# c = [random.randint(0,10) for i in range(20)] 
c = [0] * 20
for i in range(20):
    c[i] = random.randint(0,10)

print(c)

# (num - min) / (max - min)