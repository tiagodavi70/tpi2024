class Eletronico:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco
    
    def preco_com_imposto(self, p):
        return self.preco * (1 + p / 100)

    def preco_com_desconto(self, tipo):
        if tipo == "estudante":
            return self.preco - self.preco * 0.1
        elif tipo == "vip":
            return self.preco - self.preco * 0.15
        else:
            return self.preco

produto1 = Eletronico("Notebook", 3000)
produto2 = Eletronico("Smartphone", 1500)
produto3 = Eletronico("Tablet", 2000)

produtos = [produto1, produto2, produto3]

for produto in produtos:
    print(f"Modelo: {produto.modelo}")
    print(f"Preço original: {produto.preco}")
    print(f"Preço com imposto (23%): {produto.preco_com_imposto(23)}")
    print(f"Preço com desconto para estudante: {produto.preco_com_desconto('estudante')}")
    print(f"Preço com desconto para VIP: {produto.preco_com_desconto('vip')}") 