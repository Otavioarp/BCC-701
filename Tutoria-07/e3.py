'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def imprime_vetor(vetor):
    print('[ ',end='')
    for i in range(len(vetor)):
        print(f' {vetor[i]:.1f} ',end='')
    print(' ]')


print('Leitura do vetor (elementos float)... ')
x , vetor_result , vetor_sum = 1 , [] , []

x = float(input('Digite um valor -->   '))
while x > -1:
    vetor_result.append(x)
    x = float(input('Digite um valor -->   '))


for i in range(len(vetor_result)):
    somatorio = 0
    for j in range (0,i+1):
        somatorio += vetor_result[j]
    vetor_sum.append(somatorio)


print('Impressão dos Vetores Resultantes: \nVetor lido: ')
imprime_vetor(vetor_result)
print('Vetor soma acumulada: ')
imprime_vetor(vetor_sum)
