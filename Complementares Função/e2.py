'''
Otávio Augusto de Rezende Pinto
Matricula : 20.2.1385
Email: otavio.augusto@aluno.ufop.edu.br
'''
def SucessorInteiro(a):
    return a+1


def AntecessorInteiro(a):
    return a-1


num_int = int(input('Sucessor e Antecessor de um número\nDigite um número inteiro: '))

print(f'O antecessor do número é: {AntecessorInteiro(num_int)}')
print(f'O sucessor do número é: {SucessorInteiro(num_int)}')
