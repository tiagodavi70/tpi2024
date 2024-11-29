#     Escreva uma classe chamada Produto. Um Produto contém:

#     Um nome
#     Um preço
#     Uma data de validade em dias
#     Métodos que achar necessário

# Escreva as classes Shampoo, Biscoito e Leite, subclasses de Produto

#     Shampoo contém um campo que indica a irritabilidade do shampoo para peles normais (int)
#     Biscoito contém um campo que indica quantidade de componentes cancerígenos em sua fórmula (int)
#     Leite contém um campo que indica quantos dias o leite dura após ser embalado (int)
# Crie uma lista com 8 desses produtos, e uma função retorne o produto com o maior preço dessa lista.

class Produto:
    def __init__(self, nome, preco, validade):
        self.nome = nome
        self.preco = preco
        self.validade = validade

    def __str__(self):
        return f"{self.nome} | {self.preco} | {self.validade}"

class Shampoo(Produto):
    def __init__(self, nome, preco, validade, irritabilidade):
        super().__init__(nome,preco,validade)
        self.irritabilidade = irritabilidade

    def __str__(self):
        # stringBase = str(super())
        stringBase = super().__str__()
        return stringBase + f" | {self.irritabilidade}"

class Biscoito(Produto):
    def __init__(self, nome, preco, validade, componentes):
        super().__init__(nome,preco,validade)
        self.componentes = componentes

    def __str__(self):
        # stringBase = str(super())
        stringBase = super().__str__()
        return stringBase + f" | {self.componentes}"

class Leite(Produto):
    def __init__(self, nome, preco, validade, embalado):
        super().__init__(nome,preco,validade)
        self.embalado = embalado

    def __str__(self):
        # stringBase = str(super())
        stringBase = super().__str__()
        return stringBase + f" | {self.embalado}"

# Crie uma lista com 8 desses produtos, e uma função retorne o produto com o maior preço dessa lista.
# cafe = Produto("Café", 2.0, 180)
seda1 = Shampoo("Seda I", 4.0, 200, 3)
seda2 = Shampoo("Seda II", 4.5, 200, 3)
seda3 = Shampoo("Seda III", 5.0, 200, 3)

biscoito1 = Biscoito("Passatempo", 3.0, 200, 40)
biscoito2 = Biscoito("Oreo", 2.5, 200, 40)
biscoito3 = Biscoito("Continente", 1.0, 200, 40)

leite1 = Leite("Mimosa", 1.5, 200, 3)
leite2 = Leite("Hacendado", 1.2, 200, 3)

produtos = [seda1, seda2, seda3, biscoito1, biscoito2, biscoito3]

maior = produtos[0]
for i in range(len(produtos)):
    if maior.preco < produtos[i].preco:
        maior = produtos[i]
print(f"Produto com maior preço: {maior}")