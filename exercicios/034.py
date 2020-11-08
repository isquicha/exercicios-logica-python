"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
"""
a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não é uma equação do segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Delta menor que 0. Não há raízes reais.")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"Delta é zero. A raíz é {raiz}")
    else:
        raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
        raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)
        print(
            f"Delta maior que zero. A raíz 1 é {raiz1}, e a raiz 2 é {raiz2}"
        )
