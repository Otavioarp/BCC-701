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
            elif tipo == 'real':
                valor = float(colunas[j].strip())
            else:
                valor = colunas[j].strip()
            vetor.append(valor)
        matriz.append(vetor)
    return matriz



alfa = ['F' , 'E' , 'D' , 'C' , 'B' , 'A']
mat = input('Notas dos alunos: ')
tipo_n = input('Tipo de nota: ')
matriz = preencherMatriz(mat , tipo_n)
funcao_de_sair = 0
if tipo_n != 'real' and tipo_n != 'int':
    for h in range(len(alfa)):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == alfa[h]:
                    print(f'Pior nota: {alfa[h]}')
                    funcao_de_sair = 1
                    break
            if funcao_de_sair == 1:
                break
        if funcao_de_sair == 1:
            break
else:
    vet = []
    for i in range(len(matriz)):
        vet.append(min(matriz[i]))
    print(f'Pior nota: {min(vet)}')
