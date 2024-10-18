# Uma empresa de entregas cobra 4€ para cada quilômetro em uma entrega. A cada 100
# quilômetros é cobrada uma taxa extra de 10€. Também são cobrados 2€ por cada 30 quilos
# da entrega. Escreva um script de simulação, que receba um número indefinido de entregas,
# e para cada entrega receba a quilometragem e o peso das encomendas. Ao final da execução
# deve apresentar o valor total a ser pago.

# encomenda
resposta_utilizador = "s"

soma_kilometragem = 0
soma_pesos = 0

while resposta_utilizador != "n":
    kilometragem = float(input("Entra com os kilometros: "))
    peso = float(input("Entra com o peso: "))
    soma_kilometragem += kilometragem
    # soma_kilometragem = soma_kilometragem + kilometragem
    soma_pesos += peso

    resposta_utilizador = input("Deseja continuar? s/n ")

taxa_quilometragem = (soma_kilometragem // 100) * 10
custo_kilometragem = taxa_quilometragem + (soma_kilometragem * 4)

custo_peso = (soma_pesos//30) * 2

print(f"Valor total: {custo_kilometragem + custo_peso}")
