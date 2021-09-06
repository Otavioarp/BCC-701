'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
t=int(input('Entre com t: '))
n=int(input('Entre com n:'))
i,t1 = 0,0
while i <= (n-1):

    t1 += t/2**i
    i += 1

print(f'O tempo estimado é {t1:.4f}')
