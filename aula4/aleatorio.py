import random

a = random.random() # [0,1[
saida = ""
for i in range(100):
    saida += str(random.random()) + " "
# print(saida)

b = random.randint(0,10)
saida = ""
for i in range(100):
    saida += f"{random.randint(0,10)} "

print(saida) 

