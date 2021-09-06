'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''

vm=float(input('Velocidade máxima : '))
vr=float(input('Velocidade mdeda : '))
v=int(0)
p=int(0)

if vr<=(vm+10) :
    v=120
    p=2
elif vr>(vm+10) and vr<=(vm+30):
    v=250
    p=5




print(f'Multa de R$ {v:.2f} e {p} pontos na CNH ')
