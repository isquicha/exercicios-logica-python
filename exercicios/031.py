"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""
dia_int = int(input("Digite o número do dia da semana: "))
dia_str = ""
if dia_int == 1:
    dia_str = "Domingo"
elif dia_int == 2:
    dia_str = "Segunda"
elif dia_int == 3:
    dia_str = "Terça"
elif dia_int == 4:
    dia_str = "Quarta"
elif dia_int == 5:
    dia_str = "Quinta"
elif dia_int == 6:
    dia_str = "Sexta"
elif dia_int == 7:
    dia_str = "Sábado"

if dia_str == "":
    print("Valor inválido")
else:
    print(f"O dia correspondente é {dia_str}")
