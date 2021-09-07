'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
d = int(input('Comprimento da alavanca (m)'))
d1 = int(input('Distância da resistência ao fulcro (m):'))
m1 = int(input('Massa da resistência (kg)'))

print(f'Massa de equilíbrio = {m1*d1/(d-d1):.2f} Kg ')
