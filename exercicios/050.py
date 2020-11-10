"""
Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
continuar = True
while continuar:
    populacao_a = float(input("Digite a população de A: "))
    populacao_b = float(input("Digite a população de B: "))
    crescimento_a = float(
        input("Digite o crescimento percentual da população de A: ")
    )
    crescimento_b = float(
        input("Digite o crescimento percentual da população de B: ")
    )
    anos = 0
    while True:
        anos += 1
        populacao_a *= 1 + (crescimento_a / 100)
        populacao_b *= 1 + (crescimento_b / 100)
        if populacao_a >= populacao_b:
            print(
                f"Demorou {anos} anos para a população de "
                "A passar ou igualar a de B."
                f"\nA tem {populacao_a:.0f} habitantes e "
                f"B tem {populacao_b:.0f}."
            )
            break
    continuar = (
        True if input("Deseja continuar (S/N)? > ").upper() == "S" else False
    )
