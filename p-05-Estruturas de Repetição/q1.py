'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
import math
def avaliaTubo(a,b,c):
     #return True if (math.fabs(a - b)) <= c else False
     return (math.fabs(a - b)) <= c
     return False



cc=float(input('Comprimento de corte dos tubos: '))
me=float(input('Margem de erro aceitável: '))
qt=int(input('Quantidade de tubos demandada: '))
i,a,b=0,0,0

while(i != qt):
    qtc = float(input('Comprimento do tubo cortado: '))
    if avaliaTubo(qtc,cc,me):
        i+=1
        a+=1
    else:
        print('Acima da margem de erro, tubo rejeitado ')
        b+=1
print(f'''Fim da produção, demanda atendida.
Total de tubos cortados: {a+b}
Total de tubos rejeitados: {b}''')