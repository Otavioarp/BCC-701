'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
n = int(input('Informe a quantidade de repúblicas: '))
vt = 0
for i in range(0,n):
    vfr = 0
    x = int(input(f'República número {i+1}:\nQuantos produtos na lista de compras: '))
    for j in range(0,x):
        vp = float(input('Qual o valor do produto ? '))
        vfr += vp
    print(f'Compras da República {i + 1}: R$ {vfr:.2f}')
    vt += vfr
print(f'Total das compras: R$ {vt:.2f}')
