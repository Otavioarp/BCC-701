'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

km=int(input('Em qual quilômetro você se encontra? '))
pp=int(input('Quantos quilômetros pode percorrer? '))
x=km+pp
if(x<30 ):
    print(f'Vá a pé e busque combustível!\nVocê somente chegará ao km {x}')
else:    
    if((x-30)<30):
        p='A'
        g=4.30
    elif((x-60)<30 or ( km < 60 )):
        p='B'
        g=4.20
    elif((x-90)<30 and km > 60 ):
        p='C'
        g=5.10
    elif((x-120)<30):
        p='D'
        g=4.10
    print(f'Você chegará ao posto {p} , gasolina: R$ {g:.2f}')







