"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = []
for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

print("Notas digitadas: ")
for nota in notas:
    print(nota)
print(f"A média das notas é {sum(notas)/4:.2f}.")
