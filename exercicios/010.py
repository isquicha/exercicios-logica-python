"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
"""
graus_celsius = float(input("Digite a temperatura em Celsius: "))
graus_farenheit = ((graus_celsius * 9) / 5) + 32
print(
    f"{graus_celsius:.2f} graus Celsius correspondem a "
    f"{graus_farenheit:.2f} graus Farenheit"
)
