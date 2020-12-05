"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
acidentes de trânsito.

Foram obtidos os seguintes dados:
    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito
        e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de
        2.000 veículos de passeio.
"""
maior_indice = 0
codigo_maior_indice = 0
menor_indice = 100000000000000
codigo_menor_indice = 0
total_de_veiculos = 0
cidades_menos_de_2000 = 0
acidentes_cidades_menos_de_2000 = 0

for _ in range(5):
    codigo = int(input("Digite o codigo da cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio: "))
    acidentes = int(input("Digite o número de acidentes: "))

    if acidentes > maior_indice:
        maior_indice = acidentes
        codigo_maior_indice = codigo
    if acidentes < menor_indice:
        menor_indice = acidentes
        codigo_menor_indice = codigo

    total_de_veiculos += veiculos

    if veiculos < 2000:
        cidades_menos_de_2000 += 1
        acidentes_cidades_menos_de_2000 += acidentes

print(
    f"A cidade com maior índice de acidentes é a {codigo_maior_indice}"
    f" com {maior_indice} acidentes"
)
print(
    f"A cidade com menor índice de acidentes é a {codigo_menor_indice}"
    f" com {menor_indice} acidentes"
)
print(f"A média de veículos é de {total_de_veiculos/5:.2f}")
print(
    "A média de acidentes em cidades com menos de 2000 veículos é de "
    f"{acidentes_cidades_menos_de_2000/cidades_menos_de_2000:.2f}"
)
