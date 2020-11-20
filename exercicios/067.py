"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário.

O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos.

Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.
"""
numero = int(input("Digite um numero inteiro: "))
if numero == 1 or numero == 2:
    print(
        f"{numero} é primo e foram executadas 0 divisões para descobrir isso"
    )
elif numero % 2 == 0:
    print(
        f"{numero} não é primo e foi executada uma divisão para descobrir isso"
    )
else:
    contador = 1
    primo = True
    for i in range(3, numero, 2):
        contador += 1
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(
            f"{numero} é primo e foram executadas"
            f" {contador} divisões para descobrir isso"
        )
    else:
        print(
            f"{numero} não é primo e foram executadas"
            f" {contador} divisões para descobrir isso"
        )
