nome = "Tiago Davi Oliveira de Araújo"

indice = nome.find("Davi")

print(indice)

print(nome[6])

# nome[indice_inicial]
# nome[indice_inicial:indice_final:passo]

print(nome[indice:len(nome)])
print(nome[indice:])
print(nome[5:15])
print(nome[:indice])

nomes = nome.split(" ")
print(nomes)

vetor_nomes = ["Alexandre", "Freitas"]

print(" ".join(vetor_nomes))

print(nome.endswith("aújo"))
print(nome.startswith("Tia"))

