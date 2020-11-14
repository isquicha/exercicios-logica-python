"""
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
numero = 1
for _ in range(expoente):
    numero *= base
print(f"{base} elevado a {expoente} é {numero}")
