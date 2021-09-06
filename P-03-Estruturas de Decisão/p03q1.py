'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
c=float(input('Capital emprestado: '))
m=int(input('Quantidade de meses para quitação: '))

if c<=10000:
    t=0.1
elif c>10000:
    t=0.07
print(f'Taxa de juros aplicada: {t*100:.0f} %\nJuros devido: {c*t*m:.2f}\nValor total: {c*t*m+c:.2f}')
