'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
print('\tExercício 1 - Operações com Matriz ')
print('------------------------------------------------------')
dim_matriz = int(input('Qual a dimensão da matriz (n) ?   '))
matriz = []
for i in range (dim_matriz):
    linha = []
    for j in range(dim_matriz):
        elem = int(input(f'Elemento [ {i}][ {j}]:   '))
        linha.append(elem)
    matriz.append(linha)
sum_dp , pro_ds , acima_dp , abaixo_dp = 0 , 1 , 1 , 0
x = dim_matriz - 1
for i in range (dim_matriz):
    sum_dp += matriz[i][i]
    pro_ds = pro_ds * matriz[i][x]
    x -= 1

for i in range(dim_matriz):
    for j in range(i):
        if matriz[i][j] == 0:
            abaixo_dp += 1

for i in range(dim_matriz):
    for j in range( dim_matriz - ( i + 1 ) , 0 , -1):
        acima_dp = acima_dp * matriz[i][j]

print(f'''\t\tResultados
------------------------------------------------------
Somatório (diagonal principal):   {sum_dp:.2f}
Produtório (diagonal secundária):   {pro_ds:.2f}
Produtório (acima da digonal principal):   {acima_dp:.2f}
Nulos (abaixo da digonal principal):   {abaixo_dp}
''')
