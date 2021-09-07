'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
def preencherVetor(valores):
    vetor = [ ]
    valores = valores.split(',')
    for i in range(len(valores)):
        valor = float(valores[i].strip())
        vetor.append(valor)
    return vetor


def  calculosVetor(vet):
    menor, maior, media, tam = math.inf , -math.inf, 0, len(vet) 
    for i in range(tam):
        if vet[i] < menor:
            menor = vet[i]
        if vet[i] > maior:
            maior = vet[i]
        media += vet[i]
    return tam, menor, maior, media/tam


print('Manipulações de valores de Vetor ')
vet_x = preencherVetor(input('Vetor X: '))
tamanho, min, max, media_a = calculosVetor(vet_x)
print(f'''
Propriedades do vetor X:
. Possui {tamanho} elementos
. {min:.2f} é o menor valor
. {max:.2f} é o maior valor
. A média dos valores é {media_a:.2f}
''')