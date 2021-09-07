'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def PRIMO(p):
    if p%2==0 and p!=0:
        return True
n=int(input('Digite um número: '))
if PRIMO(n)== True:
    print(f'O número {n} é primo. ')
else:
    print(f'O número {n} não é primo. ')
