'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def Centena(a):
    return str(a)[1]
dc=int(input('Dígitos de uma placa automotiva\nDigite a placa do veículo (4 dígitos): '))
print(f'Dígito da(s) centena(s): {Centena(dc)}')