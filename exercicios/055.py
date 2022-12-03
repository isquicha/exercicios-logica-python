"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""
print('\nDigite dois números inteiros a seguir.\n')
numero1 = int(input('1°: '))
numero2 = int(input('2°: '))

if numero1 > numero2:
    for i in range(numero2+1, numero1):
        print(i)
else:
    for i in range(numero1+1, numero2):
        print(i)
