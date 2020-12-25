# Exercícios de Lógica de Programação em Python

## Descrição
Resolução em Python dos exercícios de Lógica de Programação e Algoritmos da [lista de exercícios da Wiki da Python Brasil](https://wiki.python.org.br/ListaDeExercicios).

## Conteúdo
1. [Exercícios de Lógica de Programação em Python](#exercícios-de-lógica-de-programação-em-python)
   1. [Descrição](#descrição)
   2. [Conteúdo](#conteúdo)
   3. [Motivação](#motivação)
   4. [Olhe também](#olhe-também)
   5. [Saiba que](#saiba-que)
   6. [Enunciados](#enunciados)
      1. [Estruturas sequenciais](#estruturas-sequenciais)
      2. [Estruturas de decisão](#estruturas-de-decisão)
      3. [Estruturas de repetição](#estruturas-de-repetição)
      4. [Listas](#listas)

## Motivação
Estou resolvendo esta lista para disponibilizar as resoluções como material complementar do meu curso de [Lógica de Programação e Algoritmos com Python](https://www.udemy.com/course/programarcompython/?referralCode=2657DAE91BF990DE780E).

## Olhe também
"Cópia" desse repositório para as linguagens:
- [C/C++](https://github.com/isquicha/exercicios-logica-c)
- [Lua](https://github.com/isquicha/exercicios-logica-lua)

Meus cursos de:
- [Programação Orientada a Objetos com Python](https://www.udemy.com/course/poocompython/?referralCode=2D98A8C4A1F3B64E6837)
- [Lógica de Programação e Algoritmos com C/C++](https://www.udemy.com/course/programarcomc/?referralCode=04DEC481E14D3EFE4B1B)
- [Lógica de Programação e Algoritmos com Lua](https://www.udemy.com/course/programarcomlua/?referralCode=E7C03C84588AAED48068)

A [licença](https://creativecommons.org/licenses/by/2.5/br/) da Wiki da Python Brasil.

## Saiba que
Como são resoluções para um curso de Lógica de Programação (nível inicante), não foram utilizadas as famosas boas práticas de programação, pois o objetivo é justamente ensinar os fundamentos de lógica, sem adicionar muita complexidade.

## Enunciados
### Estruturas sequenciais
#### [Exercicio 001](exercicios/001.py)

Faça um Programa que mostre a mensagem "Alo mundo" na tela.

#### [Exercicio 002](exercicios/002.py)

Faça um Programa que peça um número e então mostre a mensagem O número
informado foi [número].

#### [Exercicio 003](exercicios/003.py)

Faça um Programa que peça dois números e imprima a soma.

#### [Exercicio 004](exercicios/004.py)

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#### [Exercicio 005](exercicios/005.py)

Faça um Programa que converta metros para centímetros.

#### [Exercicio 006](exercicios/006.py)

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#### [Exercicio 007](exercicios/007.py)

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário.

#### [Exercicio 008](exercicios/008.py)

Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#### [Exercicio 009](exercicios/009.py)

Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre
a temperatura em graus Celsius.
C = (5 * (F-32) / 9).

#### [Exercicio 010](exercicios/010.py)

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
em graus Farenheit.

#### [Exercicio 011](exercicios/011.py)

Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.

#### [Exercicio 012](exercicios/012.py)

Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58

#### [Exercicio 013](exercicios/013.py)

Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7

#### [Exercicio 014](exercicios/014.py)

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente.

João precisa que você faça um programa que leia a variável peso
(peso de peixes) e calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.

#### [Exercicio 015](exercicios/015.py)

Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

#### [Exercicio 016](exercicios/016.py)

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.

#### [Exercicio 017](exercicios/017.py)

Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias.

#### [Exercicio 018](exercicios/018.py)

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).

### Estruturas de decisão
#### [Exercicio 019](exercicios/019.py)

Faça um Programa que peça dois números e imprima o maior deles.

#### [Exercicio 020](exercicios/020.py)

Faça um Programa que peça um valor e mostre na tela se o valor é
positivo ou negativo.

#### [Exercicio 021](exercicios/021.py)

Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#### [Exercicio 022](exercicios/022.py)

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#### [Exercicio 023](exercicios/023.py)

Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

#### [Exercicio 024](exercicios/024.py)

Faça um Programa que leia três números e mostre o maior deles.

#### [Exercicio 025](exercicios/025.py)

Faça um Programa que leia três números e mostre o maior e o menor deles.

#### [Exercicio 026](exercicios/026.py)

Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#### [Exercicio 027](exercicios/027.py)

Faça um Programa que leia três números e mostre-os em ordem decrescente.

#### [Exercicio 028](exercicios/028.py)

Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.

#### [Exercicio 029](exercicios/029.py)

As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.

#### [Exercicio 030](exercicios/030.py)

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

#### [Exercicio 031](exercicios/031.py)

Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

#### [Exercicio 032](exercicios/032.py)

Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.

#### [Exercicio 033](exercicios/033.py)

Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de
        quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;

#### [Exercicio 034](exercicios/034.py)

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

#### [Exercicio 035](exercicios/035.py)

Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.

#### [Exercicio 036](exercicios/036.py)

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.

#### [Exercicio 037](exercicios/037.py)

Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.

Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

#### [Exercicio 038](exercicios/038.py)

Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na
máquina.

Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

#### [Exercicio 039](exercicios/039.py)

Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).

#### [Exercicio 040](exercicios/040.py)

Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.

#### [Exercicio 041](exercicios/041.py)

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.

#### [Exercicio 042](exercicios/042.py)

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

#### [Exercicio 043](exercicios/043.py)

Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

#### [Exercicio 044](exercicios/044.py)

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#### [Exercicio 045](exercicios/045.py)

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne
por cliente.

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra:
    tipo de carne
    quantidade de carne
    preço total
    tipo de pagamento
    valor do desconto
    valor a pagar.

### Estruturas de repetição
#### [Exercicio 046](exercicios/046.py)

Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido.

#### [Exercicio 047](exercicios/047.py)

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.

#### [Exercicio 048](exercicios/048.py)

Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';

#### [Exercicio 049](exercicios/049.py)

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%.

Faça um programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.

#### [Exercicio 050](exercicios/050.py)

Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

#### [Exercicio 051](exercicios/051.py)

Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.

#### [Exercicio 052](exercicios/052.py)

Faça um programa que leia 5 números e informe o maior número.

#### [Exercicio 053](exercicios/053.py)

Faça um programa que leia 5 números e informe a soma e a média dos números.

#### [Exercicio 054](exercicios/054.py)

Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

#### [Exercicio 055](exercicios/055.py)

Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.

#### [Exercicio 056](exercicios/056.py)

Altere o programa anterior para mostrar no final a soma dos números.

#### [Exercicio 057](exercicios/057.py)

Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50

#### [Exercicio 058](exercicios/058.py)

Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.

#### [Exercicio 059](exercicios/059.py)

Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.

#### [Exercicio 060](exercicios/060.py)

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.

#### [Exercicio 061](exercicios/061.py)

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120

#### [Exercicio 062](exercicios/062.py)

Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.

#### [Exercicio 063](exercicios/063.py)

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

#### [Exercicio 064](exercicios/064.py)

Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e
menores que 16.

#### [Exercicio 065](exercicios/065.py)

Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo
e por 1.

#### [Exercicio 066](exercicios/066.py)

Altere o programa de cálculo dos números primos, informando, caso o número não
seja primo, por quais número ele é divisível.

#### [Exercicio 067](exercicios/067.py)

Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário.

O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos.

Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.

#### [Exercicio 068](exercicios/068.py)

Faça um programa que calcule o mostre a média aritmética de N notas.

#### [Exercicio 069](exercicios/069.py)

Faça um programa que peça para n pessoas a sua idade, ao final o programa
deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada.

#### [Exercicio 070](exercicios/070.py)

Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.

#### [Exercicio 071](exercicios/071.py)

Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de
alunos para cada turma.
As turmas não podem ter mais de 40 alunos.

#### [Exercicio 072](exercicios/072.py)

Faça um programa que calcule o valor total investido por um colecionador em sua
coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.

#### [Exercicio 073](exercicios/073.py)

O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99,
com cerca de 10 caixas.

Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma
tabela que contém o número de itens que o cliente comprou e ao lado
o valor da conta.

Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente
está levando e olhar na tabela de preços.

Você foi contratado para desenvolver o programa que monta esta
tabela de preços, que conterá os preços de 1 até 50 produtos,
conforme o exemplo abaixo:

    Lojas Quase Dois - Tabela de preços
    1 - R$ 1.99
    2 - R$ 3.98
    ...
    50 - R$ 99.50

#### [Exercicio 074](exercicios/074.py)

O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
metodologia da tabelinha, que já é um sucesso na sua loja de 1,99.

Você foi contratado para desenvolver o programa que monta a tabela de preços de
pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,
conforme o exemplo abaixo:

    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ...
    50 - R$ 9.00

#### [Exercicio 075](exercicios/075.py)

O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências.

Faça um programa que implemente uma caixa registradora rudimentar.

O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias.

Um valor zero deve ser informado pelo operador para indicar o final da compra.

O programa deve então mostrar o total da compra e perguntar o valor em dinheiro
que o cliente forneceu, para então calcular e mostrar o valor do troco.

Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a
próxima compra.

A saída deve ser conforme o exemplo abaixo:
    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00

#### [Exercicio 076](exercicios/076.py)

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.

#### [Exercicio 077](exercicios/077.py)

Desenvolva um programa que faça a tabuada de um número qualquer inteiro que
será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1
e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35

Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

#### [Exercicio 078](exercicios/078.py)

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um
programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso.

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
no campo código.

Ao encerrar o programa também deve ser informados os códigos e valores do
clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média
das alturas e dos pesos dos clientes.

#### [Exercicio 079](exercicios/079.py)

Um funcionário de uma empresa recebe aumento salarial anualmente.

Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário
inicial do funcionário.

#### [Exercicio 080](exercicios/080.py)

Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando
a sua altura em centímetros.

Encontre o aluno mais alto e o mais baixo.

Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.

#### [Exercicio 081](exercicios/081.py)

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
acidentes de trânsito.

Foram obtidos os seguintes dados:
    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito
        e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de
        2.000 veículos de passeio.

#### [Exercicio 082](exercicios/082.py)

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25

Exemplo de saída do programa:
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67

#### [Exercicio 083](exercicios/083.py)

Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100].

A entrada de dados deverá terminar quando for lido um número negativo.

#### [Exercicio 084](exercicios/084.py)

O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades
desejadas.

Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
geral do pedido.

Considere que o cliente deve informar quando o pedido deve ser encerrado.

#### [Exercicio 085](exercicios/085.py)

Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
Os códigos utilizados são:
    1, 2, 3, 4  - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.

#### [Exercicio 086](exercicios/086.py)

Desenvolver um programa para verificar a nota do aluno em uma prova com 10
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa).

Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
vai utilizar o sistema.

Após todos os alunos terem respondido informar:
    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
    Gabarito da Prova:
        01 - A
        02 - B
        03 - C
        04 - D
        05 - E
        06 - E
        07 - D
        08 - C
        09 - B
        10 - A

Após concluir isto você poderia incrementar o programa permitindo que o
professor digite o gabarito da prova antes dos alunos usarem o programa.

#### [Exercicio 087](exercicios/087.py)

Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são
eliminados.

O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe a média dos saltos conforme a
descrição acima informada (retirar o melhor e o pior salto e depois
calcular a média).

Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m

#### [Exercicio 088](exercicios/088.py)

Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes.

Você deve fazer um programa que receba o nome do ginasta e as notas dos sete
jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
média, conforme a descrição acima informada (retirar o melhor e o pior salto e
depois calcular a média com as notas restantes).

As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7

    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9,04

#### [Exercicio 089](exercicios/089.py)

Faça um programa que peça um numero inteiro positivo e em seguida mostre este
numero invertido.
Exemplo:
  12376489
  => 98467321

#### [Exercicio 090](exercicios/090.py)

Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

#### [Exercicio 091](exercicios/091.py)

Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.

### Listas

#### [Exercicio 092](exercicios/092.py)

Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

#### [Exercicio 093](exercicios/093.py)

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
inversa.

#### [Exercicio 094](exercicios/094.py)

Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

#### [Exercicio 095](exercicios/095.py)

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.

#### [Exercicio 096](exercicios/096.py)

Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.

#### [Exercicio 097](exercicios/097.py)

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.

#### [Exercicio 098](exercicios/098.py)

Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números.

#### [Exercicio 099](exercicios/099.py)

Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem
inversa a ordem lida.

#### [Exercicio 100](exercicios/100.py)

Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
a soma dos quadrados dos elementos do vetor.

#### [Exercicio 101](exercicios/101.py)

Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.

#### [Exercicio 102](exercicios/102.py)

Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

#### [Exercicio 103](exercicios/103.py)

Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.

#### [Exercicio 104](exercicios/104.py)

Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

#### [Exercicio 105](exercicios/105.py)

Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1
(que não deve ser armazenado).

Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados,
        um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados,
        um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;

#### [Exercicio 106](exercicios/106.py)

Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas
daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe
$200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:
    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante
Desafio:
    Crie ma fórmula para chegar na posição da lista a partir do salário,
    sem fazer vários ifs aninhados.

#### [Exercicio 107](exercicios/107.py)

Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo.
Para isto, faz-se necessário o desenvolvimento de um programa, que será
utilizado pelas telefonistas, para a computação dos votos.
Sua equipe foi contratada para desenvolver este programa.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma
breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:
    O total de votos computados;
    Os númeos e respectivos votos de todos os jogadores que receberam votos;
    O percentual de votos de cada um destes jogadores;
    O número do jogador escolhido como o melhor jogador da partida,
        juntamente com o número de votos e o percentual de votos dados a ele.
    Observe que os votos inválidos e o zero final não devem ser computados
        como votos.
    O resultado aparece ordenado pelo número do jogador.
    O programa deve fazer uso de arrays.
    O programa deverá executar o cálculo do percentual de cada jogador
        através de uma função. Esta função receberá dois parâmetros:
            o número de votos de um jogador e o total de votos.
    A função calculará o percentual e retornará o valor calculado.

Exemplo:
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9       4               50,0%
10      3               37,5%
11      1               12,5%
O melhor jogador foi o número 9, com 4 votos,
correspondendo a 50% do total de votos.

#### [Exercicio 108](exercicios/108.py)

Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete
feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da
enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a
entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a
percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 40% dos votos.

#### [Exercicio 109](exercicios/109.py)

As Organizações Tabajara resolveram dar um abono aos seus colaboradores em
reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os
representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

    Cada funcionário receberá o equivalente a 20% do seu salário bruto de
    dezembro;
    O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
    salário for muito baixo recebem este valor mínimo;
    Neste momento, não se deve ter nenhuma preocupação com colaboradores com
    tempo menor de casa, descontos, impostos ou outras particularidades.

Seu programa deverá permitir a digitação do salário de um número indefinido
(desconhecido) de salários.
Um valor de salário igual a 0 (zero) encerra a digitação.
Após a entrada de todos os dados o programa deverá calcular o valor do abono
concedido a cada colaborador, de acordo com a regra definida acima.
Ao final, o programa deverá apresentar:
    O salário de cada funcionário, juntamente com o valor do abono;
    O número total de funcionários processados;
    O valor total a ser gasto com o pagamento do abono;
    O número de funcionários que receberão o valor mínimo de 100 reais;
    O maior valor pago como abono;

Exemplo:
Projeção de Gastos com Abono
============================

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo foi pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00

