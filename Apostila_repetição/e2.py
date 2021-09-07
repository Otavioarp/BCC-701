'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
import math
valor = int(input('Digite um valor: '))
contador , menor , maior , somatorio = 0 , math.inf , 0 , 0
while valor > 0 :
    if valor < menor :
        menor = valor
    elif valor > maior :
        maior = valor
    contador += 1
    somatorio += valor
    valor = int(input('Digite um valor: '))
if contador > 1 :
    print(f'O menor valor informado é: {menor}')
    print(f'O maior valor informado é: {maior}')
    print(f'A média dos valores é: {somatorio / contador:.2f}')
else:
    print('Quantidade de valores insuficiente')
