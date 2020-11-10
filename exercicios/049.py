"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%.

Faça um programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
"""
populacao_a = 80_000
populacao_b = 200_000
anos = 0
while True:
    anos += 1
    populacao_a *= 1 + (3 / 100)
    populacao_b *= 1 + (1.5 / 100)
    if populacao_a >= populacao_b:
        print(
            f"Demorou {anos} anos para a população de "
            "A passar ou igualar a de B."
            f"\nA tem {populacao_a:.0f} habitantes e B tem {populacao_b:.0f}."
        )
        break
