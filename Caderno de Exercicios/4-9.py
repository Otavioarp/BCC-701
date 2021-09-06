'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
p1=int(input('Defina o valor de p1  '))
p2=int(input('Defina o valor de p2  '))
p3=int(input('Defina o valor de p3  '))
p4=int(input('Defina o valor de p4  '))
m=int(input('Defina o número mágico: '))
     

if(p1+m==p2-m==p3*m==p4/m):
    print(f'As parcelas e o número mágico formam o número quadripartido {p1+p2+p3+p4}.')
else:
    print('As parcelas e o número mágico NÃO formam um número quadripartido.')