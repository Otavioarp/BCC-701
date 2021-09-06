'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
q=int(input('Digite a quantidade de lados: '))

if q>=3:
    if 2<q<6:
        l=float(input('Digite a medida do lado: '))
        if q==3:
            print(f'O polígono é um triângulo com área: {l**2*3**(1/2)/4:.2f}')
        elif q==4:
             print(f'O polígono é um quadrado com área: {l**2:.2f}  ')
        elif q==5:
             print(f'O polígono é um pentágono com área: {3*l**2*3**(1/2)/2:.2f}  ')
    else:
        print(f'Polígono não identificado  ')
else:
    print('Não é um polígono  ')