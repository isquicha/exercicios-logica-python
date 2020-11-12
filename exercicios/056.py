"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))
somatorio = 0
for i in range(primeiro_numero + 1, segundo_numero):
    print(i)
    somatorio += i
print(f"Somatorio: {somatorio}")
