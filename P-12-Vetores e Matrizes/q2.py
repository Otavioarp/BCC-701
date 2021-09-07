'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def preencherVetor(valores, tipo='int'):
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


def comparaVetores(atual , anterior):
    vetor = []
    for i in range(len(atual)):
        if atual[i] == anterior[i]:
            x = 'E'
        elif atual[i] > anterior[i]:
            x = 'A'
        else:
            x = 'R'
        vetor.append(x)
    return vetor


def imprimeVetor(vetor):
    print('[ ',end='')
    if  len(vetor) > 0 :
        print(f'{vetor[0]}',end='')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]}',end='')
    print(' ]')


def classificaEstado(vetor):
    q_r = vetor.count('R')
    q_a = vetor.count('A')
    q_e = vetor.count('E')
    if q_r < q_a :
        x = 'Onda Vermelha'
    if q_r > q_a :
        x = 'Onda Verde'
    else:
        x = 'Onda Amarela'
    return x


num_s_anterior = preencherVetor(input('Número de mortes na semana anterior: '))
num_s_atual = preencherVetor(input('Número de mortes na semana atual: '))

if len(num_s_atual) != len(num_s_anterior):
    print(f'(Número de elementos incompatível {len(num_s_anterior)} != {len(num_s_atual)})  ')

else:
    resul = comparaVetores(num_s_atual , num_s_anterior)
    print('Classificações das macro−regiões:')
    imprimeVetor(resul)
    onda = classificaEstado(resul)
    print(f'Classificação do estado: {onda}')
