"""
Altere o programa de cálculo do fatorial (61), permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e
menores que 16.
"""
while True:
    numero = int(input("Digite um numero: "))
    if not 0 < numero < 16:
        continue
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
    if input("Deseja continuar? (S/N): ").upper() != "S":
        break
