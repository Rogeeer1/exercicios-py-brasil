'''Tendo como dado de entrada a altura (h) de uma pessoa,
 construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

h = float(input('Qual sua altura? '))
sexo = int(input('Digite seu sexo, sendo 1 para masculino / 2 para feminino: '))
if not 1 == sexo <= 2:
    print('Número inválido! ')
if sexo == 1:
    peso_ideal = (72.7*h) - 58
if sexo == 2:
    peso_ideal = (62.1*h) - 44.7

print('Seu peso ideal é: ',peso_ideal)
