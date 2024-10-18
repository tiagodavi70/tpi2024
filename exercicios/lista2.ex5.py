# Escreva um script que receba três números e mostre na tela em ordem crescente
# menor -> maior

a = int(input("Entra com o numero 1: "))
b = int(input("Entra com o numero 2: "))
c = int(input("Entra com o numero 3: "))

# 123
# 132
# 213
# 231
# 312
# 321

if a < b: # a bxc 
    if a < c and b < c:
        print(a, b, c)
    elif a < c and c < b:
        print(a, c, b)
elif b < a:
    if b < c and a < c:
        print(b, a, c)
    elif b < c and c < a:
        print(b, c, a)
elif c < a:
    if c < b and b < a:
        print(c, b, a)
    else:
        print(c, a, b)