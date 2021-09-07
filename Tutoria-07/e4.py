'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
aluno = [ 'peny', 'Rajesh koothrappali', 'Sheldon Cooper', 'Howard Wolowitz', 'Leonard Hofstadter' ]
notasbcc701 = [6, 8.5, 10, 9, 9.5 ]

print('Buscando a nota de um aluno... ')
nome = input('Digite o nome do(a) aluno(a):   ')

for i in range(len(aluno)):
    if aluno[i] == nome :
        pos = i
        print('Resultados:')
        print(f'Nome do(a) aluno(a) buscado(a): {nome} ')
        print(f'Nota: {notasbcc701[pos]:.1f}')
    else:
        if i == 4:
            print('Erro na busca, aluno(a) não encontrado(a) ! ')
