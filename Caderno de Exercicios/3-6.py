'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

p = float(input('Pressão do gás (atm)'))
v = float(input('Volume do gás (1mol)'))

t= p*v/0.082
t-=273

print(f'temperatura do gás= {p*v/0.082-273:.2f} Celsius')
