# Escreva um script que dado dois vetores indique os elementos
# que estão presentes nos dois vetores.
import random 

def elementosIguais(a, b):
    if len(a) < len(b):
        tamanho = len(a)
    else:
        tamanho = len(b)
    c = [None] * tamanho
    k = 0
    for i in range(len(a)):
        for j in range(len(b)):
            # print(a[i], b[j])
            if a[i] == b[j]:
                # print("igual", a[i])
                if a[i] not in c:
                    c[k]= a[i]
                    k = k + 1    
    i = 0 
    while i < len(c):
        if c[i] == None:
            del c[i]
        else:
            i = i + 1
    return c

a = [1, 2, 3, 4, 40, 50, 60, 8]
b = [4, 5, 6, 2]
# c = [4,2]

c = elementosIguais(a, b)
print(c)

c = [random.randint(0,10) for i in range(20)] 
d = [random.randint(0,10) for i in range(20)] 
e = elementosIguais(c, d)
print(c, d)
print(e)