'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
c=float(input('Capital emprestado: '))
m=int(input('Quantidade de meses para quitação: '))

def jurosDevido(c1,m1,t1):
    return c1*t1*m1

t=10/100 if c <= 10000 :
#t=7/100 if 10000<c<=20000 else t=5/100

print(f'Taxa de juros aplicada: {t*100:.0f}% ')
print(f'Juros devido: {jurosDevido(c,m,t):.2f} ')
print(f'Valor total: {jurosDevido(c,m,t)+c:.2f} ')