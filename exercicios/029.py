"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""
salario_anterior = float(input("Digite seu salário atual: "))
salario_atual = 0.0
diferenca_entre_salarios = 0.0
percentual_de_aumento = 0.0

if salario_anterior <= 280:
    percentual_de_aumento = 20
elif salario_anterior <= 750:
    percentual_de_aumento = 15
elif salario_anterior <= 1500:
    percentual_de_aumento = 10
else:
    percentual_de_aumento = 5

diferenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
salario_atual = salario_anterior + diferenca_entre_salarios
print(f"Seu salário antes do reajuste era de R${salario_anterior:.2f}")
print(f"Seu salário foi aumentado em {percentual_de_aumento}%")
print(f"Seu salário foi aumentado em R${diferenca_entre_salarios:.2f}")
print(f"Seu salário atual é de R${salario_atual:.2f}")
