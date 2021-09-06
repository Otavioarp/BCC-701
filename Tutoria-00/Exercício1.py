''' Otávio Augusto de Rezende Pinto
20.2.1385
otavio.augusto@aluno.ufop.edu.br      '''

p=float(input('Digite a pressão (em atm): '))
t=float(input('Digite a temperatura (em graus Celsius): '))

print(f'3 mols de um gás a {t} graus Celsius e a {p} atm, ocupam {3*0.082*(t+273.15)/p:.4f} litros')