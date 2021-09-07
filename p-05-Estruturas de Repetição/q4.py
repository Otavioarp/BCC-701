'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def verificaPerfeito(n1):
    x=0
    for i in range(1,n1-1 ):
        if n1 % i == 0 :
            x += i
        i+=1
    print(f'{n1} == {x}: número é perfeito') if x == n1 else print(f'{n1} <> {x}: número não é perfeito')


n=int(input('Digite um número: '))
while n > 0:
    verificaPerfeito(n)
    n = int(input('Digite um número: '))




