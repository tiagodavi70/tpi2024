# Escreva um script que receba o nome de uma forma geométrica, leia os dados
# necessários para cada um e imprima área e perímetro. Isso deve ser feito até receber a
# palavra “encerrar”.
# Quadrado:
# area = lado * lado
# perimetro = lado * 4
# Retângulo:
# area = largura * altura
# perimetro = 2 * largura + 2 * altura
# Círculo:
# area = 3.141592 * raio * raio
# perimetro = 2 * 3.141592 * raio

nome_forma = input("Entra com a forma ou encerrar: ")

while nome_forma != "encerrar":
    if nome_forma == "Quadrado":
        lado = float(input("Entra com o lado do quadrado:"))
        area = lado * lado
        perimetro = lado * 4
        print("Área " + str(area) + " Perímetro: " + str(perimetro))
        # print(f"Área: {area} Perímetro: {perimetro}")
    elif nome_forma == "Retangulo":
        altura = float(input("Entra com a altura: "))
        largura = float(input("Entra com a largura: "))
        area = largura * altura
        perimetro = 2 * (altura + largura)
        # print("Área " + str(area) + " Perímetro: " + str(perimetro))
        print(f"Área: {area} Perímetro: {perimetro}")
    elif nome_forma == "Circulo":
        raio = float(input("Entra com o raio: "))
        area = 3.141592 * raio**2
        perimetro = 3.141592 * 2 * raio
        # print("Área " + str(area) + " Perímetro: " + str(perimetro))
        print(f"Área: {area} Perímetro: {perimetro}")
    else:
        print("Forma não reconhecida.")
    nome_forma = input("Entra com a forma ou encerrar: ")
