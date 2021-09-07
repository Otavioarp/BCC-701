'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

nm=int(input('QUAL O NÚMERO DE MATRÍCULA ? (SOMENTE DÍGITOS): '))
matricula=str(nm)
m=matricula[:2]
n=matricula[2]
ano=int(m)
p=int(n)
if ano%2==0:
    print(f'{ano} É UM ANO PAR ')
else:
    print(f'{ano} É UM ANO ÍMPAR ')
if p==1:
    print(f'INGRESSO NO PRIMEIRO SEMESTRE')
else:
    print(f'INGRESSO NO SEGUNDO SEMESTRE')