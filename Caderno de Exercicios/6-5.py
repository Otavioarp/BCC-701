'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def DivSub(a,b):
    i=int(0)
    while a-b>=0:
        i=i+1
        a=a-b
        
    return i,a
    
a1=int(input('Digite o valor de A: '))
b1=int(input('Digite o valor de B: '))

if a1>0 and b1>0:
    q,r=DivSub(a1,b1)
    print(f'{a1} dividido por {b1}: quociente = {q}, resto = {r}')
else:
    print('ERRO: Valor(es) inválido(s) ')

