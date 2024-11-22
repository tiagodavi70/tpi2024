class Bicicleta:
    def __init__(self):
        self.marcha = 1
        self.velocidade = 0

    def mudar_marcha(self, nova_marcha):
        self.marcha = nova_marcha
    def acelerar(self, incremento):
        self.velocidade += incremento
    def frear(self):
        self.velocidade = max(0, self.velocidade - 5)
    
    def __str__(self):
        return f"Marcha: {self.marcha}, Velocidade: {self.velocidade}"


# utilização
bike = Bicicleta() # marcha 1 velocidade 0
bike.mudar_marcha(3)
bike.acelerar(15)
print(f"Marcha: {bike.marcha}, Velocidade: {bike.velocidade}")
bike.frear()
print(f"Velocidade: {bike.velocidade}")

bike2 = Bicicleta()
bike2.acelerar(30)
bike2.mudar_marcha(2)
print(f"Marcha: {bike2.marcha}, Velocidade: {bike2.velocidade}")
bike2.frear()
bike2.frear()
bike2.frear()
bike2.frear()
print(f"Marcha: {bike2.marcha}, Velocidade: {bike2.velocidade}")

print(bike)
print(bike2)

