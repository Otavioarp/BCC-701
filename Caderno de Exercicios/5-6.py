'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
na = int(input('Digite um número inteiro positivo: '))
print('Sequencia de Collatz: ')
print(f'{na:.0f}', end=' ')
while na != 1 :
    if na % 3 == 0:
        na = na / 3
        print(f'{na:.0f}', end=' ')
    elif na % 3 == 1 :
        na = (na * 4 + 2) / 3
        print(f'{na:.0f}', end=' ')
    elif na % 3 == 2:
        na = (na * 2 - 1) / 3
        print(f'{na:.0f}', end=' ')
print()
