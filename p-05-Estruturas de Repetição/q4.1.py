'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def verificaPerfeito(n1):
    x,i=0,1
    while(i!=n1):
        if n1 % i == 0 :
            x += i

        i+=1
    if x==n1:
        print(f'{n1} == {x}: número é perfeito')
    else :
        print(f'{n1} <> {x}: número não é perfeito')


n=int(input('Digite um número: '))
while n > 0:
    verificaPerfeito(n)
    n = int(input('Digite um número: '))