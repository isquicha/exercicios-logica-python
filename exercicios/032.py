"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.
"""
nota1 = float(input("Digite a primeira nota do semestre: "))
nota2 = float(input("Digite a segunda nota do semestre: "))

media = (nota1 + nota2) / 2

if media >= 9:
    aproveitamento = "A"
elif media >= 7.5:
    aproveitamento = "B"
elif media >= 6:
    aproveitamento = "C"
elif media >= 4:
    aproveitamento = "D"
else:
    aproveitamento = "E"

if aproveitamento == "D" or aproveitamento == "E":
    print(f"REPROVADO\nAproveitamento: {aproveitamento}")
else:
    print(f"APROVADO\nAproveitamento: {aproveitamento}")
