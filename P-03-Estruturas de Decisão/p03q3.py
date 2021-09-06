'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
qs=float(input('Quantidade de Morangos (em kg): '))
qa=float(input('Quantidade de Maçãs (em kg): '))

if qs >= 0 and qa >= 0:
    if qs <= 5:
        ps = qs*2.5
    elif qs > 5:
        ps = qs*2.22
    if qa <= 5:
        pa = qa * 1.8
    elif qa > 5:
        pa = qa * 1.5
    print(f'O valor total da sua compra é R$ {pa+ps:.2f} ')
else:
    print('Entrada inválida  ')
