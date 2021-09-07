'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

vc=float(input('Valor da compra '))
cp=int(input('condição de pagamento '))

if(cp==1):
    print(f'O valor da compra com 10 por cento de desconto é R$ {vc-(10/100*vc):.2f}. ')
elif(cp==2):
    print(f'O valor da compra com 5 por cento de desconto é R$ {vc-(5/100*vc):.2f}. ')
elif(cp==3):
    print(f'O valor de cada parcela é R$ {vc/2:.2f}. ')
elif(cp<1 or cp>3):
    print(f'Códico de condição de pagamento inválido ')
