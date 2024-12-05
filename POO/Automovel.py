# Crie uma classe Automovel com os atributos velocidade por hora, nome e quantos
# quilômetros foram percorridos. Crie duas classes para herdar de Automóvel, Carro e Moto.
# A classe carro deve ter um atributo que é o tipo de motor, e a classe moto deve
# ter um atributo para o tipo de farol. A classe automóvel deve ter um método dirigir,
# que recebe um argumento horas e deve adicionar nos quilômetros percorridos.
# Crie 3 carros e 3 motos e faça uma corrida entre eles,
# cada um deve dirigir por 8 horas e deve apresentar o vencedor.

class Automovel:
    def __init__(self, nome, kmPercorridos, velocidade):
        self.nome = nome
        self.kmPercorridos = kmPercorridos
        self.velocidade = velocidade
    
    def dirigir(self,horas):
        self.kmPercorridos = self.kmPercorridos + (horas * self.velocidade)

class Carro(Automovel):
    def __init__(self, nome, kmPercorridos, velocidade, tipoMotor):
        super().__init__(nome, kmPercorridos, velocidade)
        self.tipoMotor = tipoMotor


class Moto(Automovel):
    def __init__(self, nome, kmPercorridos, velocidade, farol):
        super().__init__(nome, kmPercorridos, velocidade)
        self.tipoMotor = farol

carro1 = Carro("Carro 1", 0, 60, "Gasóleo")
carro2 = Carro("Carro 2", 0, 80, "Híbrido")
carro3 = Carro("Carro 3", 0, 50, "Elétrico")

moto1 = Moto("Moto 1", 0, 40, "LED")
moto2 = Moto("Moto 2", 0, 50, "LED")
moto3 = Moto("Moto 3", 0, 45, "LED")

automoveis = [carro1, carro2, carro3, moto1, moto2, moto3]
horas = 8

for i in range(len(automoveis)):
    automoveis[i].dirigir(horas)

maior = automoveis[0]
for i in range(len(automoveis)):
    if maior.kmPercorridos < automoveis[i].kmPercorridos:
        maior = automoveis[i]

print(maior.nome)