"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))
if preco1 < preco2 and preco1 < preco3:
    print(f"O produto com o menor preco é o 1, custando R${preco1:.2f}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto com o menor preco é o 2, custando R${preco2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${preco3:.2f}")
