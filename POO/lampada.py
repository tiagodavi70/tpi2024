
class Lampada:
    def __init__(self): # construtor
        self.estado = "desligada"
        # estadoSemSelf = "Estado sem self"
    
    def ligar(self):
        self.estado = "ligada"
        # print(estadoSemSelf)
    def desligar(self):
        self.estado = "desligada"

lampada = Lampada()
print(lampada.estado) 
lampada.ligar()
print(lampada.estado)

lampada2 = Lampada()
lampada2.ligar()
print(lampada2.estado)
lampada.desligar()
print(f"Lampada 1: {lampada.estado}, lampada 2: {lampada2.estado}")