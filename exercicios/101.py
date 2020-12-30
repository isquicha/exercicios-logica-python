"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
"""
ELEMENTOS = 10
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(ELEMENTOS):
    vetor1.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 1: "))
    )
for i in range(ELEMENTOS):
    vetor2.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 2: "))
    )
for i in range(ELEMENTOS):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(ELEMENTOS * 2):
    print(vetor3[i], end=" ")
