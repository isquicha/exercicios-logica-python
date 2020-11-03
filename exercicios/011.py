"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
num3 = float(input("Digite um numero real: "))
a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print(f"a: {a}\nb: {b}\nc: {c}")
