"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
total = 0
for i in range(5):
    total += float(input("Digite um numero: "))

print(f"A média é {total/5}")
