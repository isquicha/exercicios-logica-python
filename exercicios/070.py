"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
eleitores = int(input("Digite o numero de eleitores: "))

for i in range(eleitores):
    voto = input(
        "Digite o numero (1/2/3) do candidato em quem o "
        f"eleitor {i + 1} quer votar: "
    )
    if voto == "1":
        votos_candidato_1 += 1
    if voto == "2":
        votos_candidato_2 += 1
    if voto == "3":
        votos_candidato_3 += 1
        
print("Total de votos ao condidato 1: ", votos_candidato_1)
print("Total de votos ao condidato 2: ", votos_candidato_2)
print("Total de votos ao condidato 3: ", votos_candidato_3)

if votos_candidato_1 > votos_candidato_2 > votos_candidato_3:
    print("O candidato 1 venceu!!!")

elif votos_candidato_2 > votos_candidato_1 > votos_candidato_3:
    print("O candidato 2 venceu!!!")

elif votos_candidato_3 > votos_candidato_2 > votos_candidato_1:
    print("O candidato 3 venceu!!!")
    
