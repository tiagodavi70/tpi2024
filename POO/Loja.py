# Escreva um programa em python que faça o controle de estoque de uma loja. Em um menu deve ter as opções:

# cadastrar produto
# editar produto
# vender produto
# gerar relatório

# Na opção de cadastro o utilizador deve entrar com:

#   nome do produto
#   preço
#   tipo

# Para cada produto cadastrado deve ser gerado um código. Na opção de editar deve permitir atualização do nome do produto. Na opção vender produto deve registrar uma venda do produto.
# E na opção gerar relatório deve mostrar o valor total ganho e o valor total por produto.

import random
class Produto:
    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.codigo = random.randint(0,100000000)
        
    def __str__(self):
        return f"{self.nome} | {self.preco} | {self.tipo}"


def listarProdutos(lista):
    for i in range(len(lista)):
        print(f"{i+1} - {lista[i]}")

# produtoTeste = Produto("Café", 2.0, "Alimento")
# produtoTeste.nome = "Capsulas de Café"
# print(produtoTeste)

produtos = []
vendas = []

produtos.append(Produto("Café", 2.0, "Alimento"))
produtos.append(Produto("Vinho", 4.0, "Bebida"))
produtos.append(Produto("Detergente", 3.0, "Limpeza"))

opcao = 0
while opcao != 5:
    print("Cadastro")
    print("Escolha uma das opções: ")
    print("1 - Cadastrar\n2 - Editar\n3 - Vender\n4 - Relatório\n5 - Sair")
    opcao = int(input("Opcao: "))
    if opcao == 1:
        nome = input("Entra com o nome do produto: ")
        tipo = input("Entra com o tipo do produto: ")
        preco = float(input("Entra com o preço do produto: "))
        produto = Produto(nome, preco, tipo)
        produtos.append(produto)
    elif opcao == 2:
        print("Editar Produto")
        listarProdutos(produtos)
        opcaoEditar = int(input("Selecione um número para editar produto: "))
        produtoEdicao = produtos[opcaoEditar-1]
        print(f"Editando produto: {produtoEdicao}")
        print("Aperta ENTER para deixar em branco e manter o valor atual.")
        nome = input(f"Entra com o nome do produto (atual: {produtoEdicao.nome}): ")
        tipo = input(f"Entra com o tipo do produto (atual: {produtoEdicao.tipo}): ")
        precoString = input(f"Entra com o preço do produto (atual: {produtoEdicao.preco}): ")
        preco = float(precoString) if precoString != "" else 0

        if nome != "":
            produtoEdicao.nome = nome
        if tipo != "":
            produtoEdicao.tipo = tipo
        if preco != "":
            produtoEdicao.preco = preco

        print(f"Produto atualizado: {produtoEdicao}")
    elif opcao == 3:
        print("Vender produto")
        listarProdutos(produtos)
        opcaoVenda = int(input("Selecione um item para vender: "))
        produtoVenda = produtos[opcaoVenda-1]
        vendas.append(Produto(produtoVenda.nome, produtoVenda.preco, produtoVenda.tipo))
    elif opcao == 4:
        print("Relatório")
        somaTotal = 0 
        for i in range(len(vendas)):
            print(vendas[i].preco, vendas[i])
            somaTotal += vendas[i].preco
        print(f"Rendimento total de vendas: {somaTotal}")
        
        produtosRelatados = []
        for i in range(len(vendas)):
            somaParcial = 0
            if vendas[i].nome not in produtosRelatados:
                for j in range(len(vendas)):
                    if vendas[i].nome == vendas[j].nome:
                        somaParcial += vendas[j].preco
                produtosRelatados.append(vendas[i].nome)
                print(f"Rendimento produto {vendas[i].nome}: {somaParcial}")

    elif opcao == 5:
        print("Saindo....")
    else:
        print("Selecione uma opcao válida")