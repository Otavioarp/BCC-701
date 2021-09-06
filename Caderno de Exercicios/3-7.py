'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

p = int(input('Digite a pressão do gás (em atm) '))
t = int(input('Digite a temperatura (Em Celsius) '))

print(f'3 mols de um gás a {t} Celsius e a {p} atm, ocupam {3*0.082*(t+273.15)/p:.4f} litros')
