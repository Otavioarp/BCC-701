'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
ci=int(input('Digite o seu cupom (6 dígitos): '))
c=str(ci)
m=int(c[2])
u=int(c[5])
if m <= 3:
    p1='Kit desodorante!'
elif m <= 6:
    p1='Kit perfume!'
else:
    p1='Kit loção para os pés!'

if u % 2 == 0:
    p2= f'{u} sabonete(s)'
else:
    p2= 'um cupom adicional'
print(f'Prêmio 1: {p1}\nPrêmio 2: {p2}')
