'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

qcc=float(input('Quantidade de caixas de chocolate: '))
x=int(0)
if qcc % 1 != 0 :
    print('ERRO: Quantidade de caixas inválida! ')
else:

    if qcc <= 30:
        d = 92/100
    elif qcc <= 60:
        d = 88/100
    elif qcc <= 90:
        d = 84/100
    else:
        d = 82/100
    i=qcc
    while i>=3:
        x+=d*45
        i-=3
    x+=i*15
    print(f'Pagamento sem desconto: R$ {15*qcc} ')
    print(f'Pagamento com desconto: R$ {x:.2f}')
    print(f'Você economizou R$ {15*qcc-x:.2f}')
