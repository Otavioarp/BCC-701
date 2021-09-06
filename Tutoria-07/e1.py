'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
print('\t\t Exercício 1')
print('--------------------------------------------------')
n = int(input('Qual a dimensão do vetor?   '))
v , y = [] , 1
print('Leitura dos elementos do vetor... ')
for i in range(n):
    x = float(input(f'Elemento [{i}]:   '))
    v.append(x)
    y = y * x
print(f'Resultados: ')
print('[ ',end='')
for i in range(n):
    print(f'  {v[i]}  ',end='')
print(']')
print(f'Média Aritmética:   {sum(v) / n:.4f}')
print(f'Média Geométrica:   {y ** (1/n):.4f}')
