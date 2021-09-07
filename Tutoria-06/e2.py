'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def fat2(num):
    gol = num
    for i in range(1,num + 1):
        fat = (num - i * 2)
        if fat < 2:
            break
        gol = gol * fat
    return gol


def arranjo2Simples(n , p):
    a2 = fat2(n)/fat2(n-p)
    return a2

print('2-Fatorial e Arranjo 2-simples ')

n1 = int(input('Defina n: '))
while n1 < 0:
    n1 = int(input('Valor inválido. Defina n: '))

p1 = int(input('Defina p: '))
while p1 < 0 or p1 > n1:
    p1 = int(input('Valor inválido. Defina p: '))
print(f'A2({n1},{p1}) = {arranjo2Simples(n1,p1):.2f}')
