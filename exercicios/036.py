"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.
"""
data = input("Digite uma data no formato dd/mm/aaaa: ")
# Isto separa os elementos da data em uma lista.
# O fim de um elemento se dá por uma /
# Como são 3 elementos, podemos fazer uma atribuição múltipla direta
dia, mes, ano = data.split("/")
# E aqui transformamos os valores em inteiros para facilitar comparações
dia, mes, ano = int(dia), int(mes), int(ano)

if ano < 0:
    print("Ano inválido!")
else:
    if mes < 1 or mes > 12:
        print("Mês inválido!")
    # Isto testa se o mês é um destes dentro da lista
    # Poderiam ser feitas diversas comparações utilizando o or
    # ex. mes == 1 or mes == 3...
    # Mas achei isso mais simples.
    elif mes in [1, 3, 5, 7, 8, 10, 12]:  # meses com 31 dias
        if dia > 0 and dia < 32:
            print("Data válida!")
        else:
            print("Dia inválido!")
    elif mes in [4, 6, 9, 11]:  # meses com 30 dias
        if dia > 0 and dia < 31:
            print("Data válida!")
        else:
            print("Dia inválido!")
    else:  # fevereiro
        if ano % 4 == 0:  # Ano bissexto
            if dia > 0 and dia < 30:
                print("Data válida!")
            else:
                print("Dia inválido!")
        else:  # Ano não bissexto
            if dia > 0 and dia < 29:
                print("Data válida!")
            else:
                print("Dia inválido!")
