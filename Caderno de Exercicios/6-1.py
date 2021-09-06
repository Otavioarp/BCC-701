'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def vp(a,b,c):
    return 1/3*a*b*c

l1=float(input('Digite o comprimento do lado 1: '))
l2=float(input('Digite o comprimento do lado 2: '))
h=float(input('Digite o comprimento da altura: '))

if  l1<=0 or l2<=0 or h <=0:
    print('ERRO: Entrada inválida ')
else:
    print(f'Volume da pirâmide: {vp (l1,l2,h)} ')