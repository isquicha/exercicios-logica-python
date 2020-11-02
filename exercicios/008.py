"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_mes = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_total = salario_hora * horas_trabalhadas_mes
print(
    f"Ganhando R${salario_hora:.2f} a hora, tendo trabalhado "
    f"{horas_trabalhadas_mes} horas no mês, seu salário este mês "
    f"é de R${salario_total:.2f}."
)
