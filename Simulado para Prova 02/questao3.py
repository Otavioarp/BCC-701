'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
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



print('Ministério do Meio Ambiente ')
meta = preencherVetor(input('Metas dos estados:'),'int')
plat_a = preencherMatriz(input('Plantio de árvores:'),'int')
v = plat_a[0]
for j in range(1,len(plat_a)):
    for i in range(len(plat_a[j])):
        v[i] += plat_a[j][i]
    if v[j-1] < meta[j-1]:
        print(f'Estado {j}, meta = {meta}, plantio = {v} ')
