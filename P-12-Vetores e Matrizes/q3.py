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


def contabilizarDemandas(idade):
    vetor = criarVetor(4 , 0)
    for i in range(len(idade)):
        if idade[i] >= 85:
            vetor[0] += 1
        elif idade[i] >= 65 :
            vetor[1] += 1
        elif idade[i] >= 45 :
            vetor[2] += 1
        elif idade[i] >= 18 :
            vetor[3] += 1
    return vetor


def criarVetor(qtdElemntos , valorPadrao):
    vetor = []
    for i in range(qtdElemntos):
        vetor.append(valorPadrao)
    return vetor


def avaliaAtendimento(vacinas , demanda):
    for i in range(len(demanda)):
        if vacinas[i] >= demanda[i]:
            continue
        else:
            return False
    return True


idade_hab = preencherVetor(input('Defina as idades dos habitantes:'))
demanda_faixa_etaria = contabilizarDemandas(idade_hab)

print(f'''
Demandas a serem atendidas por faixa etária:
.  >= 85.........: {demanda_faixa_etaria[0]}
.   < 85 e >= 65.: {demanda_faixa_etaria[1]}
.   < 65 e >= 45.: {demanda_faixa_etaria[2]}
.  >= 18.........: {demanda_faixa_etaria[3]}
''')

vacinas_disponiveis = preencherVetor(input('Defina as disponibilidades de vacinas: '))
atendimento = avaliaAtendimento(vacinas_disponiveis , demanda_faixa_etaria)

if atendimento:
    print('A quantidade de vacinas é suficiente.')
else:
    print('Infelizmente, precisaremos de mais vacinas.')
