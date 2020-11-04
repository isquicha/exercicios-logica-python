"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
import math

metros_quadrados = float(
    input("Digite quantos metros quadrados você vai pintar: ")
)
latas = math.ceil(metros_quadrados / 54)
preco = latas * 80
print(f"Você precisa comprar {latas:.0f} lata(s), custando R${preco:.2f}")
