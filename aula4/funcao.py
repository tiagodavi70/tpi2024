

def soma(a, b):
    return a + b

num1 = 10
num2 = 20

s = soma(num1, num2)
s2 = soma(10, 30)
s3 = soma(40, 50)

# print(s, s2, s3)

def menu():
    opcao = 0
    while (opcao > 4) or (opcao < 1):
        print("Bem vindo!")
        print("Escolha uma opção: ")
        print("1 - Ver compras")
        print("2 - Fazer compras")
        print("3 - Apagar compra")
        opcao = int(input("Opcao: "))
    return opcao

opcao = menu()
print(opcao)