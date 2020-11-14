"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""
pares = 0
impares = 0
for _ in range(10):
    if int(input("Digite um numero: ")) % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}\nÍmpares: {impares}")
