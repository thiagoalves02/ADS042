# -*- coding: utf-8 -*-
"""Lista04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19HhclbXbC8-E8g84u4iPdrlAbB_h9WTA
"""

# Disciplina: Probabilidade e Estatística
# Aluno: Thiago Gonçalves Milanez Alves
# Matrícula: 20114290004
# Lista 04

#EX01
'''#Recebendo a quantidade de lado e a medida em cm
num = int (input('Entre com a quantidade de lados: '))
cm = int (input('Entre com a medida em cm: '))

#Fazendo cálculo da área
area = num * cm

#Condição para apresentar a resposta
if (num == 3):
  print('TRIÂNGULO', area,'cm')
if (num == 4):
  print('QUADRADO', area,'cm')
if (num == 5):
  print('PENTÁGONO')'''

#EX02
'''#Recebendo a quantidade de lado e a medida em cm
num = int (input('Entre com a quantidade de lados: '))
cm = int (input('Entre com a medida em cm: '))

#Fazendo cálculo da área
area = num * cm

#Condição para apresentar a resposta
if (num < 3):
  print('NÃO É UM POLÍGONO')
if (num == 3):
  print('TRIÂNGULO', area,'cm')
if (num == 4):
  print('QUADRADO', area,'cm')
if (num == 5):
  print('PENTÁGONO')
if (num > 5):
  print('POLÍGONO NÃO IDENTIFICADO')'''


#EX03
'''#Recebendo os 3 números
num1 = int (input('Insira o primeiro número: '))
num2 = int (input('Insira o segundo número: '))
num3 = int (input('Insira o terceiro número: '))
#Alimentando a lista
lista = [num1, num2, num3]
#Condição para identificar números iguais
if (num1 == num2 or num1 == num3 or num2 == num3):
  print('Números repetidos')
#Se não tiver números iguais, vai exibir o maior número digitado através da função MAX
else:
  print('Maior número da lista: ', max(lista))'''


#EX04
'''#Recebendo a medida dos 3 lados
lado1 = input('Insira a primeira medida: ')
lado2 = input('Insira a segunda medida: ')
lado3 = input('Insira a teceira medida: ')

#Condição para identificar o tipo do Triângulo
if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
  print('Triângulo Equilátero')
if (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
  print('Triângulo Isóscele')
if (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
  print('Triângulo Escaleno')'''

#EX05
'''#Recebendo a medida dos 3 ângulos
angulo1 = int (input('Insira o primeiro ângulo: '))
angulo2 = int (input('Insira o segundo ângulo: '))
angulo3 = int (input('Insira o teceiro ângulo: '))

#Condição para identificar o tipo do Triângulo
if (angulo1 == 90 or angulo2 == 90 or angulo3 == 90):
  print('Triângulo Retângulo')
if (angulo1 > 90 or angulo2 > 90 or angulo3 > 90):
  print('Triângulo Obtusângulo')
if (angulo1 < 90 and angulo2 < 90 and angulo3 < 90):
  print('Triângulo Acutângulo')'''

#EX06
'''#Recebendo o número
numero = int (input('Insira um número: '))
#Exibindo números de 0 até o número digitado com a função RANGE
for sequencia in range(numero):
  print(sequencia)'''

#EX07
'''#Recebendo o número 
num = int (input('Entre com um número de 1 a 4: '))
#Fazendo a condição para que aceite somente número de 1 a 4 e caso contrário repita o processo para receber o número
while (num < 1 or num > 4):
  print('Entrada Inválida')
  num = int (input('Entre com um número de 1 a 4: '))
#Imprimir o resultado para números digitados de 1 a 4
else:
  print('Número digitado: ', num)'''

#EX08
'''#Iniciando a lista e recebendo o número
lista = []
num = int (input('Entre com um número inteiro: '))

#Criando a condição WHILE para que o programa rode até o 0(Zero) seja digitado
while (num != 0):
  lista.append(num)
  print('Maior número da lista: ', max(lista))
  num = int (input('Entre com um número inteiro: '))
else:
  print('Programa encerrado')'''

#EX09
'''#Recebendo o número de 4 digitos
numero = int (input('Entre com um número de 4 digitos: '))

#Extraindo a unidade
unidade = numero % 10

#Retirando a unidade
numero = (numero - unidade)/10

#Extraindo a dezena
dezena = numero % 10

#Retirando a dezena
numero = (numero - dezena)/10

#Extraindo a centena
centena = numero % 10

#Retirando a centena
numero = (numero - centena)/10

#Resta o milhar
milhar = numero

#Tornando-os inteiro
dezena = int(dezena)
centena = int(centena)
milhar = int(milhar)

#Exibindo os dados
print('Unidade=', unidade, 'Dezena=', dezena, 'Centena=', centena, 'Milhar=', milhar)'''