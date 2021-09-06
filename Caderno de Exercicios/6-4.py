'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def myfu(c,j,a,ir):
    return c*(1+j)**a-(c*(1+j)**a-c)*ir , (c*(1+j)**a-(c*(1+j)**a-c)*ir - c)/c*100
c1=float(input('Capital a ser investido: '))
j1=float(input('Taxa de juros anual do investimento: '))
a1=int(input('Número de anos do investimento: '))
ir1=float(input('Imposto sobre o lucro: '))
vf,l= myfu(c1,j1,a1,ir1)
print(f'Valor final = {vf:.2f}\nPercentual de lucro líquido = {l:.2f}%')
