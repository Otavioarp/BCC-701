'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''
def SucessorInteiro(a):
    return a+1


def AntecessorInteiro(a):
    return a-1


num_int = int(input('Sucessor e Antecessor de um número\nDigite um número inteiro: '))

print(f'O antecessor do número é: {AntecessorInteiro(num_int)}')
print(f'O sucessor do número é: {SucessorInteiro(num_int)}')
