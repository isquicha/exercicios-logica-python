"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.
"""
ALUNOS = 30
idades = []
alturas = []
media_de_altura = 0
abaixo_da_media = 0

for i in range(ALUNOS):
    idades.append(int(input(f"Digite a idade do aluno {i+1}: ")))
    altura = int(input(f"Digite a altura em cm do aluno {i+1}: "))
    alturas.append(altura)
    media_de_altura += altura

media_de_altura /= ALUNOS

for i in range(ALUNOS):
    if idades[i] > 13:
        if alturas[i] < media_de_altura:
            abaixo_da_media += 1

print(
    f"{abaixo_da_media} alunos com mais de 13 anos têm altura abaixo da média"
)
