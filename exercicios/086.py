"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa).

Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
vai utilizar o sistema.

Após todos os alunos terem respondido informar:
    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
    Gabarito da Prova:
        01 - A
        02 - B
        03 - C
        04 - D
        05 - E
        06 - E
        07 - D
        08 - C
        09 - B
        10 - A

Após concluir isto você poderia incrementar o programa permitindo que o
professor digite o gabarito da prova antes dos alunos usarem o programa.
"""
# * Imports
# ? Possibilita saber se o PC roda windows ou linux
from sys import platform

# ? A função system possibilita exercutar comandos no terminal
from os import system

# * Variáveis globais
aluno_com_maior_acerto = ""
aluno_com_menor_acerto = ""
maior_acerto = 0
media_da_turma = 0
numero_de_alunos = 0
# ? O gabarito e os alunos vão ser dicionários Python
# ? Dicionários guardam conteúdos no formato "chave": valor
gabarito = {}
alunos = {}

numero_de_questoes = int(input("Digite o número de questões: "))
menor_acerto = numero_de_questoes

# * Programa
# ? i vai de 1 até o número de questões
for i in range(1, numero_de_questoes + 1):
    # ? O .upper() garante que a resposta vai ser sempre uma letra maiuscula
    resposta_atual = input(
        f"Digite a resposta correta da questão '{i}': "
    ).upper()
    # ? Guarda a resposta correta no gabarito
    # ? Por exemplo, se i = 2 e resposta_atual = "A", e a resposta da questao 1
    # ? (que foi preenchida na rodada anterior do laço for) for "C"
    # ? então: gabarito = {"questao_1": "C", "questao_2": "A"}
    gabarito["questao_" + str(i)] = resposta_atual

if platform == "win32":
    limpar = "cls"
else:
    limpar = "clear"

while True:
    # ? Limpa a tela para os alunos não verem o gabarito, nem a resposta
    # ? dos colegas
    system(limpar)

    aluno = input("Digite o nome do aluno (ou 0 para sair): ")
    if aluno == "0":
        system(limpar)
        break

    numero_de_alunos += 1

    # ? Cria o dicionario de respostas e nota do aluno
    alunos[aluno] = {"acertos": 0}

    for i in range(1, numero_de_questoes + 1):
        resposta_atual = input(
            f"Digite a resposta que o aluno {aluno} deu para a questão {i}: "
        ).upper()
        # ? Guarda a resposta do aluno no dicionário de respostas dele
        alunos[aluno]["questao_" + str(i)] = resposta_atual

# ? Vamos percorrer cada aluno e suas respostas
for aluno, respostas in alunos.items():
    # ? E percorrer cada uma de suas respostas
    for questao, resposta in respostas.items():
        if questao == "acertos":
            continue
        # ? Se a resposta for igual ao gabarito
        if resposta == gabarito[questao]:
            alunos[aluno]["acertos"] += 1

    acertos = alunos[aluno]["acertos"]
    nota = 10 * acertos / numero_de_questoes
    print(
        f"O aluno {aluno} obteve {acertos} acertos dentre {numero_de_questoes}"
        f" questões e ficou com a nota {nota:.2f}"
    )

    if acertos > maior_acerto:
        maior_acerto = acertos
        aluno_com_maior_acerto = aluno
    if acertos < menor_acerto:
        menor_acerto = acertos
        aluno_com_menor_acerto = aluno

    media_da_turma += nota

media_da_turma /= numero_de_alunos
print(
    f"O aluno com o mais acertos é {aluno_com_maior_acerto}, "
    f"com {maior_acerto} acertos"
    f"\nO aluno com o menos acertos é {aluno_com_menor_acerto}, "
    f"com {menor_acerto} acertos"
    f"\nA média da turma é {media_da_turma:.2f}"
)
