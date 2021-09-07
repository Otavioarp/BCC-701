'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
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


def criarVetor(qtdElemntos , valorPadrao):
    vetor = []
    for i in range(qtdElemntos):
        vetor.append(valorPadrao)
    return vetor

print('Organizações Trambaqui ')

jogos = ['Mega-Sena' , 'Diplasena' , 'Lotomania' ]
ma = input('Defina a matriz: ')
mat = preencherMatriz(ma,'float')

for i in range(len(mat)):
    while len(mat[i]) != 3 or len(mat) < 4 :
        print('Matriz incorreta ')
        ma = input('Defina a matriz: ')
        mat = preencherMatriz(ma,'float')

soma_total = 0 
soma_linha = criarVetor(len(mat[0]),0)
for i in range(len(mat)):
    
    for j in range(len(mat[i])):
        soma_total += mat[i][j]
        soma_linha[j] += mat[i][j]

for i in range(len(soma_linha)):
    print(f'{jogos[i]} R$ {soma_linha[i]:.2f}')
print(f'Total de prêmios: R$ {soma_total:.2f}')
