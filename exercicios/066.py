"""
Altere o programa de cálculo dos números primos, informando, caso o número não
seja primo, por quais número ele é divisível.
"""
numero = int(input("Digite um numero inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f"{numero} não é primo! É divisível por {i}.")
if primo:
    print(f"{numero} é primo!")
