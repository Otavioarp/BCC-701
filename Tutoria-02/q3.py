'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def Centena(a):
    return str(a)[1]
dc=int(input('Dígitos de uma placa automotiva\nDigite a placa do veículo (4 dígitos): '))
print(f'Dígito da(s) centena(s): {Centena(dc)}')