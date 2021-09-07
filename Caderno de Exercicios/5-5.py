'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
t=int(input('Entre com t: '))
n=int(input('Entre com n:'))
i,t1 = 0,0
while i <= (n-1):

    t1 += t/2**i
    i += 1

print(f'O tempo estimado é {t1:.4f}')
