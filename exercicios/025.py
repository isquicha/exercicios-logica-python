"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
numero3 = float(input("Digite mais um numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} foi o maior numero digitado.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} foi o maior numero digitado.")
else:
    print(f"{numero3} foi o maior numero digitado.")

if numero1 < numero2 and numero1 < numero3:
    print(f"{numero1} foi o menor numero digitado.")
elif numero2 < numero1 and numero2 < numero3:
    print(f"{numero2} foi o menor numero digitado.")
else:
    print(f"{numero3} foi o menor numero digitado.")
