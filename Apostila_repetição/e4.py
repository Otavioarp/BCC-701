'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

if x < y :
    j = x
else:
    j = y
for i in range (j,0,-1):
        if x % i == 0 and y % i == 0:
            mdc = i
            break
print(f'O MDC é: {mdc}')
