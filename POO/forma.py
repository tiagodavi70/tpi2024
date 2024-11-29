class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


# Criar o Circulo e o Quadrado
# Utilização
retangulo = Retangulo(5, 3)
print(f"Área do Retângulo: {retangulo.calcular_area()}")
