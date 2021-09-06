'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

i = float(input('Digite a taxa de juros: '))
c = float(input('Digite o capital investido: '))
n = int(input('Digite o período de investimento: '))

print(f'O valor do montante é :{c*((1+i)**n):.2f}')
