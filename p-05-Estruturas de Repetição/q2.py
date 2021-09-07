'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def Fatorial(a):
    x=1
    while (1 != a):
        x = x * a
        a -= 1
    return x

n=int(input('Informe o número que deseja calcular o Fatorial: '))
while (n <= 0 ):
    n=int(input('Número inválido, defina outro: '))
print(f'O Fatorial de {n} é: {Fatorial(n)} ')