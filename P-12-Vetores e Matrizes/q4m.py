'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def preencherVetor(valores, tipo = 'int'):
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


def preencherMatriz(valores, tipo = 'int'):
    matriz = []
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        vetor = preencherVetor(linhas[lin],tipo)
        matriz.append(vetor)
    return matriz


def pontuao( resultados):
    tam = len(resultados)
    vetor = criarVetor(tam , 0)
    for i in range(tam):
        for j in range(tam):
            if resultados[i][j] == 1:
                vetor[i] += 3
            elif resultados[i][j] == 2:
                vetor[j] += 3
            elif resultados[i][j] == 0:
                vetor[i] += 1
                vetor[j] += 1
    return vetor


def criarVetor(qtdElemntos , valorPadrao):
    vetor = []
    for i in range(qtdElemntos):
        vetor.append(valorPadrao)
    return vetor



nomes_times = preencherVetor(input('Nomes dos times: '),'string')
resultados_jogos = preencherMatriz(input('Resultados dos jogos: '))
vet_pont = pontuao(resultados_jogos)
ind_max = vet_pont.index(max(vet_pont))
print(f'Time campeão: {nomes_times[ind_max]}')
print(f'Pontuação do campeão: {max(vet_pont)}')
