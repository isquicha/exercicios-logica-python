"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.
"""
caracteres = []
consoantes = 0
for i in range(10):
    caracteres.append(input("Digite um caractere: ")[0])

for c in caracteres:
    c = c.upper()
    if c != "A" and c != "E" and c != "I" and c != "O" and c != "U":
        consoantes += 1

print(f"Foram lidas {consoantes} consoantes.")
