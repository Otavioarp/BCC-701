'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br

'''

vp=float(input('velocidade maxima '))
v=float(input('velocidade do veiculo '))


if(v>vp and v<=(vp+10)):
    pts=2
    m=120
elif(v>(vp+10) and v<=(vp+30)):
    pts=5
    m=250
elif(v>(vp+30)and v<=300):
    pts=7
    m=600
    
if(v<=vp):
    print(f'Motorista não cometeu infração')
elif(v<=0 or v>300):
    print(f'Velocidade invalida')
else:
    print(f'Multa de R$ {m:.2f} e {pts} pontos na CNH' ) 