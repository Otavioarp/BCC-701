'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
n = int(input('Anne Bonny, defina N: '))
e = int(input('Barba Negra, defina E: '))
t = int(input('Barba Negra, defina X: '))
a = 1
for i in range (0,t):
    h = int(input(f'Anne Bonny, escolha um número entre {a} e {n}]: '))
    if h == e:
        print(f'Anne Bonny você ganhou, o número é {e}!')
        break
    elif h < e:
        a = h
    else:
        n = h
    if i == 2:
        print(f'Anne Bonny você consumiu suas {t} tentativas, Barba Negra ganhou!')
