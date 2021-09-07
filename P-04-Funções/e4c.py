'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def calculaArea(q1,l1):
    if q1==3:
        return 'triângulo',l1**2*3**(1/2)/4
    elif q1==4:
        return 'quadrado',l1**2
    else:
        return 'pentágono',3*l1**2*3**(1/2)/2

q=int(input('Digite a quantidade de lados: '))
if  q<3:
    print('Não é um polígono ')
elif q>5:
    print('Polígono não identificado ')
else:
    
    l=float(input('Digite a medida do lado: '))
    a,b=calculaArea(q,l)
    print(f'O polígono é um {a} com área: {b:.2f} ')