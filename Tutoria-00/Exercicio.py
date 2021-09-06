import math

r=int(input('Digite o raio do reservatório de combustível: '))
h=int(input('Digite a altura do reservatório de combustível: '))
v=float(input('Digite a capacidade (m3)do tanque dos caminhões: '))

print(f'O volume do reservatório é {math.pi*r**2*h:.2f} m3\n{int((math.pi*r**2*h)/v):.0f} Caminhões poderão ser abastecidos com este reservatório')
