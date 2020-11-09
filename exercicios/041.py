"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
op = input("Digite qual operação (+, -, * ou /) deseja realizar: ")
if op == "+":
    resultado = numero1 + numero2
elif op == "-":
    resultado = numero1 - numero2
elif op == "*":
    resultado = numero1 * numero2
elif op == "/":
    resultado = numero1 / numero2
else:
    resultado = 0

print("\nO resultado é: ")

if (resultado // 1) % 2 == 0:
    print("Par")
else:
    print("Ímpar")

if resultado >= 0:
    print("Positivo")
else:
    print("Negativo")

if resultado % 1 == 0:
    print("Inteiro")
else:
    print("Decimal")
