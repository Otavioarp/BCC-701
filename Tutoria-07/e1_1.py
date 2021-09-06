'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

print('\t\t Exercício 1')
print('--------------------------------------------------')
v = input('Quais são os elementos do vetor?(separados por ,)   ')
vetor , y = [] , 1
vetor = []
v = v.split(',')
for i in range(len(v)):
    valor = float(v[i].strip())
    vetor.append(valor)

print(f'Resultados: ')
print('[ ',end='')
for i in range(len(vetor)):
    print(f'  {vetor[i]}  ',end='')
print(']')
print(f'Média Aritmética:   {sum(vetor) / len(vetor):.4f}')
print(f'Média Geométrica:   {y ** (1/len(vetor)):.4f}')
