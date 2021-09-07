'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def preencherVetor(valores,tipo):

    vetor = []
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int' :
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def preencherMatriz(valores , tipo):
    matriz = []
    linhas = valores.split(';')
    for i in range(len(linhas)):
        colunas = linhas[i].split(',')
        vetor = []
        for j in range(len(colunas)):
            if tipo == 'int':
                valor = int(colunas[j].strip())
            elif tipo == 'float':
                valor = float(colunas[j].strip())
            else:
                valor = colunas[j].strip()
            vetor.append(valor)
        matriz.append(vetor)
    return matriz


def notasAlunos(vetor , matriz):
    notas = []
    for i in range(len(matriz)):
        cont  = 0
        tam = len(vetor)
        for j in range(tam):
            if vetor[j] == matriz[i][j]:
                cont += 1
        x = cont * 10 / tam
        notas.append(tam)
    return notas


def imprimeVetor(vetor):
    print('[ ',end='')
    if  len(vetor) > 0 :
        print(f'{vetor[0]:.2f}',end='')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]:.2f}',end='')
    print(' ]')



print('Notas de BCC701')
print('Digite o gabarito: ')
gaba = input('>>> ')
gabarito = preencherVetor(gaba,'')

print('Digite as respostas dos alunos: ')
resp_alunos = input('>>> ')
if resp_alunos == '':
    print('Nenhum aluno para avaliar ')
else:
    r_alunos = preencherMatriz(resp_alunos,'')
    if len(r_alunos[0]) != len(gabarito):
        print('Quantidade de questões incompatível ')
    else:
        notas_f = notasAlunos(gabarito , r_alunos)
        print('Notas dos alunos: ')
        imprimeVetor(notas_f)
