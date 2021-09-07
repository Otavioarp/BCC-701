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


def calculaLucros(v_quibe , v_coxinha , l_quibe , l_coxinha):
    vetor = []
    for i in range(len(v_quibe)):
        vetor.append((v_quibe[i] * l_quibe )+(v_coxinha[i] * l_coxinha))
    return vetor


def imprimeVetor(vetor):
    print('[ ',end='')
    if  len(vetor) > 0 :
        print(f'{vetor[0]:.2f}',end='')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]:.2f}',end='')
    print(' ]')


vendas_c = input('Vendas de coxinhas: ')
coxinhas_vendidas = preencherVetor(vendas_c,'int')

vendas_q = input('Vendas de quibes: ')
quibes_vendidos = preencherVetor(vendas_q,'int')

if len(quibes_vendidos) != len(coxinhas_vendidas):
    print('Dados de vendas inválidos ')

else:
    lucro_coxinha = float(input('Lucro por unidade de coxinha: R$ '))
    lucro_quibe = float(input('Lucro por unidade de quibe: R$ '))
    lucro_total = calculaLucros(quibes_vendidos , coxinhas_vendidas ,lucro_quibe , lucro_coxinha )
    print('Lucros: ',end='')
    imprimeVetor(lucro_total)
    print(f'Maior lucro: R$ {max(lucro_total):.2f}')
    print(f'Menor lucro: R$ {min(lucro_total):.2f}')
