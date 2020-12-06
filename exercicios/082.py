"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25

Exemplo de saída do programa:
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
"""
valor_da_divida = float(input("Digite o valor da dívida: "))
parcelas = 1
juros = 0
print(
    "|Valor da Dívida|Valor dos Juros|Quantidade de Parcelas|Valor da Parcela|"
)
while True:
    # ? A fórmula abaixo foi encontrada usando a equação da reta
    # ? y - y0 = m * (x - x0), com y = 15, y= = 10, x = 6 e x0 = 3
    # ? y -> Percentual de juros | x -> Quantidade de parcelas
    juros = (5 / 3) * parcelas + 5
    # ? Não é uma reta perfeita pois quando x=1, y=0
    if parcelas == 1:
        juros = 0

    valor_do_juros = valor_da_divida * (juros / 100)
    valor_total = valor_da_divida + valor_do_juros
    valor_da_parcela = valor_total / parcelas
    print(
        f"|R$ {valor_total:.2f}\t"
        f"|R$ {valor_do_juros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valor_da_parcela:.2f}"
    )
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    if parcelas > 12:
        break
