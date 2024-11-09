# Escreva uma função que adicione um valor em um vetor somente se ele não estiver presente.

def verificarPresenca(vetor, numero):

    adicionar = True
    for i in range(len(vetor)):
        if vetor[i] == numero:
            adicionar = False

    if adicionar:
        adicionado = False
        for i in range(len(vetor)):
            if vetor[i] == None and not adicionado:
                vetor[i] = numero
                adicionado = True

    return adicionar

a = [None] * 5

verificarPresenca(a, 5)
verificarPresenca(a, 4)
verificarPresenca(a, 3)
verificarPresenca(a, 4)
verificarPresenca(a, 4)
verificarPresenca(a, 7)
verificarPresenca(a, 7)
verificarPresenca(a, 4)
verificarPresenca(a, 3)
verificarPresenca(a, 8)

print(a) # = [5, 4, 3]