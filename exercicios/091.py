"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.
"""
h = 0
for i in range(1, int(input("Digite o numero de termos: ")) + 1):
    h += 1 / i

print(f"H = {h}")
