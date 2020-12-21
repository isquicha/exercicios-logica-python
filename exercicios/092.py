"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i+1}º numero: ")))

print("Os numeros digitados são:", end="")
for numero in lista:
    print(f" {numero}", end="")
