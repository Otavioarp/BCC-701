'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

def criarVetor(qtdElemntos , valorPadrao):
    vetor = []
    for i in range(qtdElemntos):
        vetor.append(valorPadrao)
    return vetor


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
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        vetor = preencherVetor(linhas[lin],tipo)
        matriz.append(vetor)
    return matriz


def maisVendido(vendas):
    vetor = criarVetor(len(vendas),0)
    for i in range(len(vendas)):
        for j in range(len(vendas[i])):
            vetor[i] += vendas [i][j]
        
    return vetor


nomes_produtos = preencherVetor(input('Nomes dos produtos: '),'string')
qnt_vendas = preencherMatriz(input('Quantidades de vendas: '),'int')
somatorio = maisVendido(qnt_vendas)
vmax = max(somatorio)
ind = somatorio.index(vmax)
print(f'Produto selecionado: {nomes_produtos[ind]}')
print(f'Total de vendas do produto: {somatorio[ind]}')
