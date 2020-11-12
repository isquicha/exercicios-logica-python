"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""
primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))
for i in range(primeiro_numero + 1, segundo_numero):
    print(i)
