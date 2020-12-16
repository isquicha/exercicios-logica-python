"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes.

Você deve fazer um programa que receba o nome do ginasta e as notas dos sete
jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
média, conforme a descrição acima informada (retirar o melhor e o pior salto e
depois calcular a média com as notas restantes).

As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7

    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9,04
"""
NOTAS = 7
atletas = []
while True:
    nome = input("\nDigite o nome do atleta ou 0 para sair: ")
    if nome == "0":
        break
    atleta = {
        "nome": nome,
        "notas": [],
        "media": 0,
        "melhor_nota": 0,
        "pior_nota": 0,
    }
    for i in range(NOTAS):
        atleta.get("notas").append(float(input("Nota: ")))
    atleta.get("notas").sort()
    atleta["melhor_nota"] = atleta.get("notas").pop()
    atleta["pior_nota"] = atleta.get("notas").pop(0)
    media = sum(atleta.get("notas"))
    media /= NOTAS - 2
    atleta["media"] = media
    atletas.append(atleta)

print("\nResultado final:")
for atleta in atletas:
    print(f"Atleta: {atleta.get('nome')}")
    print(f"Melhor nota: {atleta.get('melhor_nota')}")
    print(f"Pior nota: {atleta.get('pior_nota')}")
    print(f"Média: {atleta.get('media'):.2f}")
