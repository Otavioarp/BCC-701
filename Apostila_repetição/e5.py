'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
n = int(input('Digite o valor de N: '))
for i in range(2,n+1):
    contador = 0
    for j in range(1,i+1):
        if i % j == 0:
            contador += 1
    if contador == 2:
        print(i)
