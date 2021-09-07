'''
Otávio Augusto de Rezende Pinto
Email: otaviopqsi@gmail.com
'''

def valida_dados():
    linha = int(input('Informe a linha: '))
    vlinha = 0 < linha and linha < 9
    while vlinha != True:
        print('Valor inválido, deve estar no intervalo [1, 8]. ')
        linha = int(input('Informe a linha: '))
        vlinha = 0 < linha and linha < 9

    coluna = int(input('Informe a coluna: '))
    vcoluna = 0 < coluna and coluna < 9
    while vcoluna != True:
        print('Valor inválido, deve estar no intervalo [1, 8]. ')
        coluna = int(input('Informe a coluna: '))
        vcoluna = 0 < coluna and coluna < 9
    return linha , coluna


l , c = valida_dados()
print('Movimentos possíveis: ')
print('     1  2  3  4  5  6  7  8  ')
print('   -------------------------')
for i in range (1,9):
    print(f'{i} |',end='')
    for j in range (1,9):
        if l == i or c == j:
            print('  1',end='')
        else:
            print('  0',end='')
    print()
