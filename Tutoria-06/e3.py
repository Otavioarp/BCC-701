'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def numerador (k):
    return (-2) ** (k +1)


def denominador(k):
    return 3 * k ** 2-1


print('Cálculos de F ')
n = int(input('Quantidade de termos N: '))
while  4 < n < 21:
    sun = 0
    for i in range(1 , n+1):
        sun += numerador(i) / denominador(i)
    print(f'Força imaginária F = {sun}')
    n = int(input('Quantidade de termos N: '))
else:
    print('Fim do programa. ')
