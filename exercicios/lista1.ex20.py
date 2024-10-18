# Um trem se locomove há 150 km/h, e funciona por 20 horas por dia.
# A cada 2.000 km ele deve parar 6 horas para manutenção.
# Cada manutenção custa R$ 2.000,00 e a cada 3 dias é cobrada uma taxa de 
# R$ 5.000,00 de uso da ferrovia. Escreva em um script que receba o número 
# de dias e escreva na tela um relatório, com o número de kilômetros 
# percorridos e manutenções realizadas, assim como o custo total.

dias = int(input("Entra com o número de dias: "))

kilometragem = 150
horas_manutencao = 6

kilometros_dias = (dias * 20) * kilometragem
manutencoes_realizadas = kilometros_dias // 2000
custo_manutencao = manutencoes_realizadas * 2000

kilometros_dias = kilometros_dias - (manutencoes_realizadas * horas_manutencao) * kilometragem
custo_kilometros = (dias//3) * 5000
custo_total = custo_manutencao + custo_kilometros

print("KM percorridos: ", kilometros_dias)
print("Manutencoes Realizadas: ", manutencoes_realizadas)
print("Custo Total: ", custo_total)
