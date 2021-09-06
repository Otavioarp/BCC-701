'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
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


def linhaMenorValor(matriz):
    minimo = math.inf
    for i in range(len(matriz)):
        mi = min(matriz[i])
        if mi < minimo :
            mini = i
            minimo = mi
    return mini


def colunaMaiorValor(matriz , ind):
    maximo = -math.inf
    for i in range(len(matriz)):
        if matriz[ind][i] > maximo:
            maxi = i
            maximo = matriz[ind][i]
    return maxi


print('MinMax de uma Matriz ')
print('Valores da matriz:')
val = input('>>> ')
mat = preencherMatriz(val , 'int')
linha_min = linhaMenorValor(mat)
coluna_max = colunaMaiorValor(mat , linha_min)
print(f'MinMax: [{linha_min}, {coluna_max}] = {mat[linha_min][coluna_max]}')
