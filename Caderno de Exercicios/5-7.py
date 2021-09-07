'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''


r1 = int(input('Digite o primeiro termo da série: '))
r2 = int(input('Digite o segundo termo da série:'))

while r1 < 0 or r2 < 0:
    r1 = int(input('Os valores informados devem ser positivos. Digite novamente.\nDigite o primeiro termo da série: '))
    r2 = int(input('Digite o segundo termo da série:'))
print(((r1 * r2) ** 2))
a1 , a2 = r1 , r2
while a2 < (r1 * r2) ** 2:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print(f'{a2}' ,end=' ') if a2 < (r1 * r2) ** 2 else print() 
print('')
