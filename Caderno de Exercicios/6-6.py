'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def PRIMO(p):
    if p%2==0 and p!=0:
        return True
n=int(input('Digite um número: '))
if PRIMO(n)== True:
    print(f'O número {n} é primo. ')
else:
    print(f'O número {n} não é primo. ')
