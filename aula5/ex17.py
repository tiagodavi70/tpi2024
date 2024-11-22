# Escreva uma função que receba uma matrix (m,n) 
# e para cada linha retorne média e somatório.

m = int(input("Entra com o número de linhas: "))
n = int(input("Entra com o número de colunas: "))
import random 
matriz = [ [random.randint(0,10) for _ in range(n)] 
          for __ in range(m)]

matriz = [ [None for _ in range(n)] for __ in range(m)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = random.random()

vetor = [0 for i in range(15)]
for i in range(len(vetor)):
    print(vetor[i])


for i in range(m):
    media = 0
    somatorio = 0
    for j in range(n):
        somatorio = somatorio + matriz[i][j]
    media = somatorio / n
    print(f"Linha {i+1}: {media}, {somatorio}")


class Colaborador:
    def __init__(self, primeiro_nome, sobrenome, salario_mensal):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        if salario_mensal > 0:
            self._salario_mensal = salario_mensal
        else:
            self._salario_mensal = 0.0

    def get_salario_mensal(self):
        return self._salario_mensal

    def set_salario_mensal(self, value):
        if value > 0:
            self._salario_mensal = value
        else:
            self._salario_mensal = 0.0

    def salario_anual(self):
        return self.salario_mensal * 12


colaborador = Colaborador("João", "Silva", 2500)
print(f"Salário mensal: {colaborador.salario_mensal}")
print(f"Salário anual: {colaborador.salario_anual()}")

colaborador.salario_mensal = -500
print(f"Novo salário mensal: {colaborador.salario_mensal}")