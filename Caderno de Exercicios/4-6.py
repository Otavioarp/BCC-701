'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
va=float(input('Digite o valor dos depósitos mensais: '))
tx=float(input('Digite a taxa de rendimento mensal: '))
n=int(input('Digite o número de meses: '))

if(va>0 and tx>0 and n%2==0): 
    print(f'Valor do rendimento após 24 meses: R$ {(va*(1+tx))*(((1+tx)**n-1)/tx):.2f} \nAplicação confirmada. ')
else:
    print('Foi encontrado algum erro nos dados de entrada.\nAplicação não confirmada.')