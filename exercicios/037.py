"""
Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.

Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
for numero in [
    326,
    300,
    100,
    320,
    310,
    305,
    301,
    101,
    311,
    111,
    25,
    20,
    10,
    21,
    11,
    1,
    7,
    16,
]:
    # O laço for foi utilizado apenas para o teste automático dos valores
    # você pode fazer os testes manualmente.
    # Basta retirar tudo de dentro do laço e descomentar a linha abaixo!
    # numero = int(input("Digite um inteiro menor que 1000: "))
    print(f"\nNumero: {numero}")
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    separador1 = ""
    separador2 = ""
    # Se tivermos ambos unidade, dezena e centena
    if centena > 0 and dezena > 0 and unidade > 0:
        separador1 = " , "  # Precisamos de uma vírgula
        # Os espaços entre as aspas são importantes
        separador2 = " e "  # E de um e
    # Senão, se tivermos uma centena e uma dezena
    elif centena > 0 and dezena > 0:
        separador1 = " e "  # Precisamos só do e, na frente
        separador2 = ""
    # Já se tivermos só a centena e a unidade, ou só a dezena e a unidade
    elif (centena > 0 and unidade > 0) or (dezena > 0 and unidade > 0):
        separador1 = ""  # Não haverá separador entre centena e dezena
        separador2 = " e "  # Mas sim entre centena/dezena e unidade
    # Nos outros casos só temos um dos três valores,
    # e os separadores podem continuar sendo vazios ("")

    # Se a centena não estiver zerada
    if centena > 0:
        if centena == 1:
            # Se ela for igual a 1, colocamos nela por extenso no singular
            centena = "1 centena"
        else:
            # Senão, colocamos ela por extenso no plural
            centena = f"{centena} centenas"
    else:
        # Se estiver zerada, colocamos nela uma string
        # vazia para nada ser impresso
        centena = ""
    # Mesa coisa para a dezena
    if dezena > 0:
        if dezena == 1:
            dezena = "1 dezena"
        else:
            dezena = f"{dezena} dezenas"
    else:
        dezena = ""
    # Mesa coisa para a unidade
    if unidade > 0:
        if unidade == 1:
            unidade = "1 unidade"
        else:
            unidade = f"{unidade} unidades"
    else:
        unidade = ""

    # Importante observar que podemos fazer esse algoritmo facilmente em
    # Python por ser uma linguagem dinâmicamente tipada, ou seja, se eu
    # quiser mudar o valor de uma variável que era do tipo inteiro para um
    # valor do tipo string ou qualquer outro eu posso
    # Em linguagens como C++ seria necessário declarar 2 variáveis:
    # 1 para o número e outra para o texto

    # Por fim printamos o resultado
    print(f"{centena}{separador1}{dezena}{separador2}{unidade}")
