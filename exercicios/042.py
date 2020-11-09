"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
positivos = 0
resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Mora perto da vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1

if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")
