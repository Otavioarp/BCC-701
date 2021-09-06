'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
n_alunos = int(input('Digite o número de alunos: '))
med_a = 0
for i in range(0,n_alunos):
    nome = input(f'Digite o nome do aluno {i+1}: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    nota_3 = float(input('Nota 3: '))
    med_p = (nota_1 * 3+nota_2 * 4+nota_3* 5) / 12
    print(f'Média Ponderada das notas de {nome}: {med_p:.3f}\n')
    med_a += med_p
print(f'Média da turma:{med_a / n_alunos:.3f}')
