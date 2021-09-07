'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
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


print('Hipermercados Compra Fácil ')
print('Diferenças de vendas: ')

vd = input('>>> ')
vendas = preencherMatriz(vd , 'float')
bairros = ['Morro do Cruzeiro' , 'Jardim Alvorada' 
, 'Cabeças']
secoes = ['Massas' , 'Esportes' , 'Cereais' , 'Eletrônicos' ]



print('\nRelatório de baixas de vendas ')
for i in range(len(vendas)):
    print(f'Bairro {bairros[i]}')
    for j in range(len(vendas[i])):
        if vendas[i][j] < 0 :
            print(f'\t.Seção: {secoes[j]} ')
    print()
