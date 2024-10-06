idade = int(input("Entra com tua idade: "))

if idade > 0 and idade <= 5:
    print("Não paga")
elif idade > 5 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 27:
    print("Jovem")
elif idade > 27 and idade <= 60:
    print("Adulto")
else:
    print("Idoso")