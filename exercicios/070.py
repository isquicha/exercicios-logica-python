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
        f"eleitor {i} quer votar: "
    )
    if voto == "1":
        votos_candidato_1 += 1
    if voto == "2":
        votos_candidato_2 += 1
    if voto == "3":
        votos_candidato_3 += 1

print(
    "Votação encerrada"
    f"Candidato 1: {votos_candidato_1} votos"
    f"Candidato 2: {votos_candidato_2} votos"
    f"Candidato 3: {votos_candidato_3} votos"
)
