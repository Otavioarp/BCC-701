'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def ler_vetor(  ):
    valores = input('Digite o vetor com os valores separados por , : ')
    vetor = []
    valores = valores.split(',')
    for i in range(len(valores)):
            valor = float(valores[i].strip())
            vetor.append(valor)
    return vetor


def imprimi_vetor(vetor):
    print('[ ',end='')
    for i in range(len(vetor)):
        print(f' {vetor[i]:.1f} ',end='')
    print(' ]')


print('\t\t Exercício 2')
print('--------------------------------------------------')
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
for i in range(len(vetor_1)):
    print(f' {(vetor_1[i]+vetor_2[i])*2:.1f} ',end='')
print('] ')
