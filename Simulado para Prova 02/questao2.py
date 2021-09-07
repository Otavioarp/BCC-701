'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def preencherMatriz(valores):
    matriz = []
    linhas = valores.split(';')
    for i in range(len(linhas)):
        colunas = linhas[i].split(',')
        vetor = []
        for j in range(len(colunas)):
            valor = int(colunas[j].strip())
            vetor.append(valor)
        matriz.append(vetor)
    return matriz


def imprimeMatriz(matriz):
    if len(matriz) > 0 :
        imprimeVetor(matriz[0])
        print('')
        for lin in range(1,len(matriz)):
            imprimeVetor(matriz[lin])
            print('')


def imprimeVetor(vetor):
    print('[ ',end='')
    if  len(vetor) > 0 :
        print(f'{vetor[0]:.2f}',end='')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]:.2f}',end='')
    print(' ]')


print('Loja da tia Maria ')
mat_e = preencherMatriz(input('Matriz de estoque:'))
n_a = int(input('Número de atualizações: '))
for i in range(n_a):
    ind_l = int(input('Índice da loja: '))
    ind_p = int(input('Índice do produto: '))
    n_e = int(input('Novo estoque: '))
    mat_e[ind_l][ind_p] = n_e
    imprimeMatriz(mat_e) 