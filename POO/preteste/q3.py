class Automovel:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f"Nome: {auto.nome}, Tipo: {auto.tipo}"

automoveis = [None] * 10
for i in range(10):
    nome = input(f"Digite o nome do automóvel {i+1}: ")
    tipo = input(f"Digite o tipo do automóvel {i+1}: ")
    automoveis[i] = Automovel(nome, tipo)

print("\nLista de Automóveis:")
for auto in automoveis:
    print(auto)