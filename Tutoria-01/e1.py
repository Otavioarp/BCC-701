'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
vc=float(input('INFORME O VALOR DA COMPRA: '))

if vc<=150:
    d=10/100*vc
    
if vc>=150:
    d=20/100*vc
i=8/100*(vc-d)
print(f'VALOR DO DESCONTO:            R$ {d:.2f}')
print(f'VALOR DA COMPRA COM DESCONTO: R$ {vc-d:.2f}')
print(f'VALOR DO IMPOSTO:             R$ {i:.2f}')
print(f'TOTAL A PAGAR:                R$ {vc-d+i:.2f}')


