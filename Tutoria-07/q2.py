'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def ler_vetor(  ):
    vetor = []
    for i in range(dim_vec):
        x = int(input(f'Elemento na posição {i}:  '))
        vetor.append(x)
    return vetor
def imprimi_vetor(vetor):
    print('[ ',end='')
    for i in range(len(vetor)):
        print(f' {vetor[i]:.1f} ',end='')
    print(' ]')
print('\t\t Exercício 2')
print('--------------------------------------------------')
global dim_vec
dim_vec = int(input('Qual a dimensão dos vetores?   '))
print('Leitura do primeiro vetor... ')
vetor_1 , vetor_2 = [] , []
vetor_1 = ler_vetor()
print(f'Leitura do segundo vetor... ')
vetor_2 = ler_vetor()
print('Vetor 1')
imprimi_vetor(vetor_1)
print(f'Vetor 2')
imprimi_vetor(vetor_2)
print(f'Vetor 3')
print('[ ',end='')
for i in range(dim_vec):
    print(f' {(vetor_1[i]+vetor_2[i])*2:.1f} ',end='')
print('] ')
