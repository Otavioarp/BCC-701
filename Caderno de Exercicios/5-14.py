'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
n = int(input('Informe o número de avaliações: '))
nome = str(input('\nNome do(a) aluno(a) '))
sun , sunpeso = 0 , 0
while nome != '':
    for i in range(0,n):
        nota = float(input(f'Nota {1 + i}: '))
        peso = int(input(f'Peso {i + 1}: '))
        sun += nota * peso
        sunpeso += peso
    med = sun  / sunpeso
    if med < 3:
        print(f'{nome} está reprovado(a) com média {med:.2f}.')
    elif med < 6:
        print(f'{nome} está em exame especial com média {med:.2f}.')
    else:
        print(f'{nome} está aprovado(a) com média {med:.2f}.')
    nome = str(input('Nome do(a) aluno(a) '))
