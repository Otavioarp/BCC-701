'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

p=float(input('Digite seu peso (em kg):  '))
h=float(input('Digite sua altura (em metros):  '))
cq=float(input('Digite a circunferência do seu quadril (em cm):  '))

print(f'IMC = {p/h**2:.3f}  ')
print(f'IAC = {cq/h**(3/2)-18:.3f}  ')