"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
notas = 0
contador = 0
continuar = "S"
while continuar == "S":
    nota = float(input("Digite uma nota: "))
    notas += nota
    contador += 1
    continuar = input("Deseja continuar? (S/N): ").upper()

print(f"A média das notas é {notas/contador:.2f}.")
