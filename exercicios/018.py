"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""
tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade da conexão em Mbps: "))
tempos = (tamanho * 8) / velocidade
minutos = tempos // 60
segundos = tempos % 60
print(f"{minutos:.0f} Minutos e {segundos:.0f} Segundos")
