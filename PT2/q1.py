'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
import math
def calculaNota(nota):
    menor , soma  = math.inf , 0 
    for i in range(len(nota)):
        if nota[i] < menor:
            menor = nota[i]
            x = i
    nota.pop(x)
    for i in range(len(nota)):
        soma += notas[i]
    return soma/len(nota)


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


provas = ['Boxe' , 'Ciclismo' , 'Hipismo' , 'Ginástica']

print('Jogos da Juventude de Seul \n')
for i in range(len(provas)):
    print(f'Prova: {provas[i]}')
    print('\t. Digite as notas dos 5 juízes: ')
    nt = input('\t>>> ')
    notas = preencherVetor(nt,'float')
    nota_f = calculaNota(notas)
    print(f'\t. Nota final: {nota_f:.4f}\n')