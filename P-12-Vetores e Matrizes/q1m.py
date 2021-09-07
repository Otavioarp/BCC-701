'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def converterVetorMatriz (vetor):
    n = len(vetor)
    i = 1
    while i != n :

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


def preencherVetor(valores, tipo):
    vetor = [ ]
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def preencherMatriz(valores, tipo):
    matriz = []
    linhas = valors.split(';')
    for lin in range(len(linhas)):
        vetor = preencherVetor(linhas[lin],tipo)
        matriz.append(vetor)
    return matriz


vet = preencherVetor(input('Entrada do vetor: '),'int')
mat = converterVetorMatriz(vet)
imprimeMatriz(mat)
