# Escreva um algoritmo que receba do utilizador o nome de uma pessoa, seu ano de nascimento e o ano atual.
# Como saída, exiba o nome da pessoa e sua idade atual;

nome = input("Entra com teu nome: ")

ano_nascimento = input("Entra com teu ano de nascimento: ")
ano_nascimento = int(ano_nascimento)

idade = 2024 - ano_nascimento

print(nome, "tem", idade, "anos")