class Colaborador:
    def __init__(self, primeiro_nome, sobrenome, salario_mensal):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        if salario_mensal > 0:
            self._salario_mensal = salario_mensal
        else:
            self._salario_mensal = 0.0

    def get_salario_mensal(self):
        return self._salario_mensal

    def set_salario_mensal(self, value):
        if value > 0:
            self._salario_mensal = value

    def salario_anual(self):
        return self._salario_mensal * 12
    
    def aumentar5Porcento(self):
        self._salario_mensal = self._salario_mensal * 5/100 + self._salario_mensal

    def salarioComImposto(self, imposto):
        return self.get_salario_mensal() - imposto


# a) Escreva uma função que aumente em 5% o salário do colaborador.
# b) Escreva uma função retorne o valor dos salário descontado de um valor n de imposto.

colaborador = Colaborador("João", "Silva", 2500)
print(f"Salário mensal: {colaborador.get_salario_mensal()}")
print(f"Salário anual: {colaborador.salario_anual()}")

colaborador.set_salario_mensal(-500)
print(f"Novo salário mensal: {colaborador.get_salario_mensal()}")

colaborador.aumentar5Porcento()
print(f"Novo salário mensal: {colaborador.get_salario_mensal()}")

print(colaborador.salarioComImposto(300))