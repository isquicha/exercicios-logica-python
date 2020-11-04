"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias.
"""
import math

metros_quadrados = float(input("Digite os m²: "))
metros_quadrados_mais_dez = metros_quadrados * 1.0

rendimento_litro = 6
litros_lata = 18
preco_lata = 80
rendimento_lata = rendimento_litro * litros_lata
litros_galao = 3.6
preco_galao = 25
rendimento_galao = rendimento_litro * litros_galao

somente_latas = math.ceil(metros_quadrados / rendimento_lata)
somente_galoes = math.ceil(metros_quadrados / rendimento_galao)
latas = math.floor(metros_quadrados_mais_dez / rendimento_lata)
galoes = math.ceil(
    (metros_quadrados_mais_dez % rendimento_lata) / rendimento_galao
)

print(
    f"Somente Latas: {somente_latas}, "
    f"custando R${somente_latas * preco_lata}\n"
    f"Somente Galões: {somente_galoes}, "
    f"custando R${somente_galoes * preco_galao}\n"
    f"Latas: {latas} , Galões: {galoes}, "
    f"custando R${((latas * preco_lata) + (galoes *preco_galao)):.2f}"
)
