'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

r1=6
r2=8
r3=10

v= int(input('Digite o valor tensão (V)  '))
r4 = int(input('Digite o valor  da resistência 4 (omhs)'  ))

req=r1+r2+r3+r4
qd4=r4/req*v
pd4=r4/req*v**2

print(f'V4 = {r4/req*v:.4f} V \nP4 = {r4/req*v**2:.4f} W')
