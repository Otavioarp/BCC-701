'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
va=float(input('Digite o valor dos depósitos mensais: '))
tx=float(input('Digite a taxa de rendimento mensal: '))
n=int(input('Digite o número de meses: '))

if(va>0 and tx>0 and n%2==0): 
    print(f'Valor do rendimento após 24 meses: R$ {(va*(1+tx))*(((1+tx)**n-1)/tx):.2f} \nAplicação confirmada. ')
else:
    print('Foi encontrado algum erro nos dados de entrada.\nAplicação não confirmada.')