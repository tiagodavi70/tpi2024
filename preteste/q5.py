# A loja OAZ Sports apresenta um conjunto de descontos que
# depende do tipo e a quantidade de itens comprados.
# Para cada 4 peças do tipo vestuário o cliente ganha 2% de
# desconto, e para cada 2 peças de calçados ganha 3% de desconto. Escreva um script que simule um
# caixa, que leia um produto de cada vez com seu preço e tipo, e no final aplique o desconto
# sobre a compra total

soma_valor_vestuario = 0
soma_valor_calcado = 0
quant_vestuario = 0
quant_calcado = 0

resposta_utilizador = "s"

while resposta_utilizador == "s":
    tipo = input("vesturario ou calcado?")
    preco = float(input("Entra com o valor"))
    
    if tipo == "vestuario":
        soma_valor_vestuario = soma_valor_vestuario + preco
        quant_vestuario = quant_vestuario + 1
    elif tipo == "calcado":
        soma_valor_calcado = soma_valor_calcado + preco
        quant_calcado = quant_calcado + 1
    
    resposta_utilizador = input("Deseja continuar? s/n ")

desconto_vestuario = (quant_vestuario // 4) * (2/100) * soma_valor_vestuario
soma_valor_vestuario = soma_valor_vestuario - desconto_vestuario

desconto_calcado = (quant_calcado // 2) * (3/100) * soma_valor_calcado
soma_valor_calcado = soma_valor_calcado - desconto_calcado

print("Valor total: " + str(soma_valor_calcado + soma_valor_vestuario))