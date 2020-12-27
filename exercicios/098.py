"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números.
"""
inteiros = []
soma = 0
multiplicacao = 1
for i in range(5):
    numero = int(input(f"Digite o {i+1}º inteiro: "))
    soma += numero
    multiplicacao *= numero
    inteiros.append(numero)

print("\nNúmeros digitados:")

for numero in inteiros:
    print(f"{numero}", end=" ")

print(f"\nA soma dos números é {soma}")
print(f"A multiplicação dos números é {multiplicacao}")
