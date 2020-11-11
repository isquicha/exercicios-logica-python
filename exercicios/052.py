"""
Faça um programa que leia 5 números e informe o maior número.
"""
# Existem várias formas de se resolver este problema, e adotei aqui uma forma
# mais voltada a Lógica do quê a praticidade.

# Vamos precisar da constante 'infinito' da biblioteca matemática
from math import inf

# Neste não faz sentido usar estrutura de repetição sem utiliza listas
numeros = []  # Uma lista de números vazia
for i in range(5):
    numero = float(input("Digite um número (serão 5 ao todo): "))
    numeros.append(numero)  # Coloca o número digitado na lista de números

# Iniciamos um número com o menor valor possível, neste caso, menos infinito
maior_numero = -inf
# Colocar um valor muito pequeno ao invés de infinito pode dar certo também,
# desde que o usuário não digite todos os valores menores do que este primeiro
# valor setado. Por isso usamos o -infinito, pois não tem nada menor que isso.

# Para cada número na lista de números
for numero in numeros:
    # Se o número atual for maior do que o maior número guardado
    if numero > maior_numero:
        # Então o número atual passa a ser o maior número
        maior_numero = numero

print(maior_numero)
