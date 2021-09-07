'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
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
        print(f'{vetor[0]:}',end='')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]}',end='')
    print(' ]')


def exameEspecial(vetor):
    vetor_exame = []
    for i in range(len(vetor)):
        if  3 <= vetor[i] < 6 :
            vetor_exame.append(i)
    return vetor_exame


notas = input('Notas: ')
nomes = input('Nomes: ')
vetor_notas = preencherVetor(notas, 'float')
vetor_nomes = preencherVetor(nomes, '')
max , min , media = estatNotas(vetor_notas)
ind_acima = acimaMedia(vetor_notas , media)
ind_alunos_exame = exameEspecial(vetor_notas)

print(f'Maior nota: {max:.1f}')
print(f'Menor nota: {min:.1f}')
print(f'Nota média: {media:.1f}')

print(f'Índices das notas acima da média:')
imprimeVetor(ind_acima)

print(f'Notas acima da média: \n[ ',end='')
if  len(ind_acima) > 0 :
    print(f'{vetor_notas[ind_acima[0]]:.1f}',end='')
    print(f' ({vetor_nomes[ind_acima[0]]})',end='')
for i in range(1 , len(ind_acima)):
    print(f', {vetor_notas[ind_acima[i]]:.1f}',end='')
    print(f' ({vetor_nomes[ind_acima[i]]})',end='')
print(' ]')

print(f'Índices das notas para Exames Especiais: ')
imprimeVetor(ind_alunos_exame)

print(f'Notas para Exames Especiais: \n[ ',end='')
if len(ind_alunos_exame) > 0 :
    print(f'{vetor_notas[ind_alunos_exame[0]]:.1f}',end='')
    print(f' ({vetor_nomes[ind_alunos_exame[0]]})',end='')
    for i in range(1 , len(ind_alunos_exame)):
        print(f', {vetor_notas[ind_alunos_exame[i]]:.1f}',end='')
        print(f' ({vetor_nomes[ind_alunos_exame[i]]})',end='')
print(' ]')
