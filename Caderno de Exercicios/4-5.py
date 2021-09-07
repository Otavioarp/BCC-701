'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
v=float(input(' Entre com o valor da passagem: '))
c=int(input('Entre com o número do cupom de brinde(0-3): '))

if(c==0):
    vf=v
elif(c==1):
    vf=95/100*v
elif(c==2):
    vf=92.5/100*v
elif(c==3):
    vf=90/100*v
else:
    print(f'ERROR: Cupom inválido')
if(0>v<3):
    print(f'Valor da Passagem após o desconto R$ {vf:.2f} ')
    
print('Formas de pagamento\n1 − pagamento à vista sem acréscimo\n2 − em 5 vezes com acréscimo de 3 %\n3 − em 10 vezes com acréscimo de 5 %')
fp=int(input(f'Forma de pagamento '))

if(fp==1):
    vf=vf
    np=1
elif(fp==2):
    vf=103/100*vf
    np=5
elif(fp==3):
    vf=105/100*vf
    np=10
else:
    print(f'ERRO: Forma de pagamento invãlida ')
if(0<fp<4):
    print(f'Valor final da passagem R$ {vf:.2f} em {np} parcelas de R$ {vf/np:.2f} ')
    
    
    
