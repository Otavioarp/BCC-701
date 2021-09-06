
def preencherVetor(valores, tipo):
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


def estatNotas(vetor):
    med = 0
    for i in range(len(vetor)):
        med += vetor[i]
    x = min(vetor)
    y = max(vetor)
    return y , x , med/len(vetor)


def acimaMedia(vetor_notas , valor_corte):
    vetor_ind_acima = []
    for i in range (len(vetor_notas)):
        if vetor_notas[i] > valor_corte:
            vetor_ind_acima.append(i)
    return vetor_ind_acima

def imprimeVetor(vetor):

    print('[ ',end='')
    if  len(vetor) > 0 :
        print(f'{vetor[0]:.0f}',end='')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]:.0f}',end='')
    print(' ]')


notas = input('Notas: ')

vec = preencherVetor(notas ,'float')

max , min , media = estatNotas(vec)

ind_acima = acimaMedia(vec , media)

print(f'Maior nota: {max:.1f}')
print(f'Menor nota: {min:.1f}')
print(f'Nota média: {media:.1f}')

print(f'Índices das notas acima da média:')
imprimeVetor(ind_acima)

print(f'Notas acima da média: \n[ ',end='')
if  len(ind_acima) > 0 :
    print(f'{vec[ind_acima[0]]:.1f}',end='')
for i in range(1 , len(ind_acima)):
    print(f', {vec[ind_acima[i]]:.1f}',end='')
print(' ]')
