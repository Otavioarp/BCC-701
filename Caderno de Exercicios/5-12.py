'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
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
