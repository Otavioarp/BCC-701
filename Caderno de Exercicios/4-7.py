'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

c=input('Cargo: ')
t=int(input('Tempo: '))
s=float(input('Salário: '))
print(c)


    
if(s>998):
    print(c)
    if(c=='gerente'):
        if(t<=2):
            r=10/100*s
        elif(2<t<=5):
            r=9/100*s
        elif(t>5):
            r=15/100*s
    elif(c=='engenheiro'):
        if(t<=2):
            r=9/100*s
        elif(2<t<=5):
            r=10/100*s
        elif(t>5):
            r=11/100*s
        
    else:
        r=6/100*s
        
    print(f'Reajuste : R$ {r:.2f}\nSalário Reajustado : R$ {s+r:.2f} ')
else:
    print('Salãrio inválido !')
