'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

mf=float(input('Entre com a sua média final em BCC701: '))
ad=int(input('Entre com o número de aulas dadas: '))
af=int(input('Entre com sua quantidade de faltas nas aulas: '))

f=100-(af * 100 / ad)
if mf < 6 and f >= 75 :
    av=int(input('Em quantos por cento das avaliações você faltou? '))
    if av < 50 :
        print('Você poderá fazer Exame Especial Parcial ou Exame Especial Total. ')
    else:
        print('Você poderá fazer o Exame Especial Total. ')
    
    
    
    
elif f < 75 :
    print('Infelizmente você reprovou por faltas. ')
    
else:
    print('Parabéns, você foi aprovado em BCC701! ')
    