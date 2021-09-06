
def imprimeRetangulo( h ,l ):
    print()
    for i in range (0,h):
        for j in range(0,l):
            print('*',end='')
        print()


cond = input('Deseja imprimir um retângulo? (s/n) ')

while cond == 's':
    alt = int(input('\nAltura do retângulo: '))
    larg = int(input('Largura do retângulo: '))
    while alt < 1 or larg < 1 or larg <= alt :
        alt = int(input('Entrada inválida.\n\nAltura do retângulo: '))
        larg = int(input('Largura do retângulo: '))
    imprimeRetangulo(alt , larg)
    cond = input('\nDeseja imprimir outro retângulo? (s/n) ')
