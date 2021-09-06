'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
tp=int(input('Qual o tipo de ladrilho (1/2/3)? '))

if 0<tp<4:
    asa=float(input('Qual a área (cm2) da sala? '))
    if tp==1:
        ql=asa/80        
    if tp==2:
        ql=asa/60    
    if tp==3:
        ql=asa/40
    print(f'Quantidade de ladrilhos: {math.ceil(ql):.0f} ')
else:
    print('ERRO: o ladrilho tipo {tp} não é inválido.')


